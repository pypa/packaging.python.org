================================
Analyzing PyPI package downloads
================================

This section covers how to use the public PyPI download statistics dataset
to learn more about downloads of a package (or packages) hosted on PyPI. For
example, you can use it to discover the distribution of Python versions used to
download a package.

.. contents:: Contents
   :local:


Background
==========

PyPI does not display download statistics for a number of reasons: [#]_

- **Inefficient to make work with a Content Distribution Network (CDN):**
  Download statistics change constantly. Including them in project pages, which
  are heavily cached, would require invalidating the cache more often, and
  reduce the overall effectiveness of the cache.

- **Highly inaccurate:** A number of things prevent the download counts from
  being accurate, some of which include:

  - ``pip``'s download cache (lowers download counts)
  - Internal or unofficial mirrors (can both raise or lower download counts)
  - Packages not hosted on PyPI (for comparisons sake)
  - Unofficial scripts or attempts at download count inflation (raises download
    counts)
  - Known historical data quality issues (lowers download counts)

- **Not particularly useful:** Just because a project has been downloaded a lot
  doesn't mean it's good; Similarly just because a project hasn't been
  downloaded a lot doesn't mean it's bad!

In short, because it's value is low for various reasons, and the tradeoffs
required to make it work are high, it has been not an effective use of
limited resources.

Public dataset
==============

As an alternative, the `Linehaul project <https://github.com/pypa/linehaul-cloud-function/>`__
streams download logs from PyPI to `Google BigQuery`_ [#]_, where they are
stored as a public dataset.

Getting set up
--------------

In order to use `Google BigQuery`_ to query the `public PyPI download
statistics dataset`_, you'll need a Google account and to enable the BigQuery
API on a Google Cloud Platform project. You can run the up to 1TB of queries
per month `using the BigQuery free tier without a credit card
<https://cloud.google.com/blog/products/data-analytics/query-without-a-credit-card-introducing-bigquery-sandbox>`__

- Navigate to the `BigQuery web UI`_.
- Create a new project.
- Enable the `BigQuery API
  <https://console.developers.google.com/apis/library/bigquery-json.googleapis.com>`__.

For more detailed instructions on how to get started with BigQuery, check out
the `BigQuery quickstart guide
<https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui>`__.


Data schema
-----------

Linehaul writes an entry in a ``bigquery-public-data.pypi.file_downloads`` table for each
download. The table contains information about what file was downloaded and how
it was downloaded. Some useful columns from the `table schema
<https://console.cloud.google.com/bigquery?pli=1&p=bigquery-public-data&d=pypi&t=file_downloads&page=table>`__
include:

+------------------------+-----------------+-----------------------------+
| Column                 | Description     | Examples                    |
+========================+=================+=============================+
| timestamp              | Date and time   | ``2020-03-09 00:33:03 UTC`` |
+------------------------+-----------------+-----------------------------+
| file.project           | Project name    | ``pipenv``, ``nose``        |
+------------------------+-----------------+-----------------------------+
| file.version           | Package version | ``0.1.6``, ``1.4.2``        |
+------------------------+-----------------+-----------------------------+
| details.installer.name | Installer       | pip, :ref:`bandersnatch`    |
+------------------------+-----------------+-----------------------------+
| details.python         | Python version  | ``2.7.12``, ``3.6.4``       |
+------------------------+-----------------+-----------------------------+


Useful queries
--------------

Run queries in the `BigQuery web UI`_ by clicking the "Compose query" button.

Note that the rows are stored in a partitioned, which helps
limit the cost of queries. These example queries analyze downloads from
recent history by filtering on the ``timestamp`` column.

Counting package downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following query counts the total number of downloads for the project
"pytest".

::

    #standardSQL
    SELECT COUNT(*) AS num_downloads
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE file.project = 'pytest'
      -- Only query the last 30 days of history
      AND DATE(timestamp)
        BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        AND CURRENT_DATE()

+---------------+
| num_downloads |
+===============+
| 26190085      |
+---------------+

To only count downloads from pip, filter on the ``details.installer.name``
column.

::

    #standardSQL
    SELECT COUNT(*) AS num_downloads
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE file.project = 'pytest'
      AND details.installer.name = 'pip'
      -- Only query the last 30 days of history
      AND DATE(timestamp)
        BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        AND CURRENT_DATE()

+---------------+
| num_downloads |
+===============+
| 24334215      |
+---------------+

Package downloads over time
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To group by monthly downloads, use the ``TIMESTAMP_TRUNC`` function. Also
filtering by this column reduces corresponding costs.

::

    #standardSQL
    SELECT
      COUNT(*) AS num_downloads,
      DATE_TRUNC(DATE(timestamp), MONTH) AS `month`
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE
      file.project = 'pytest'
      -- Only query the last 6 months of history
      AND DATE(timestamp)
        BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH), MONTH)
        AND CURRENT_DATE()
    GROUP BY `month`
    ORDER BY `month` DESC

+---------------+------------+
| num_downloads | month      |
+===============+============+
| 1956741       | 2018-01-01 |
+---------------+------------+
| 2344692       | 2017-12-01 |
+---------------+------------+
| 1730398       | 2017-11-01 |
+---------------+------------+
| 2047310       | 2017-10-01 |
+---------------+------------+
| 1744443       | 2017-09-01 |
+---------------+------------+
| 1916952       | 2017-08-01 |
+---------------+------------+

Python versions over time
~~~~~~~~~~~~~~~~~~~~~~~~~

Extract the Python version from the ``details.python`` column. Warning: This
query processes over 500 GB of data.

::

    #standardSQL
    SELECT
      REGEXP_EXTRACT(details.python, r"[0-9]+\.[0-9]+") AS python_version,
      COUNT(*) AS num_downloads,
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE
      -- Only query the last 6 months of history
      DATE(timestamp)
        BETWEEN DATE_TRUNC(DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH), MONTH)
        AND CURRENT_DATE()
    GROUP BY `python_version`
    ORDER BY `num_downloads` DESC

+--------+---------------+
| python | num_downloads |
+========+===============+
| 3.7    | 18051328726   |
+--------+---------------+
| 3.6    | 9635067203    |
+--------+---------------+
| 3.8    | 7781904681    |
+--------+---------------+
| 2.7    | 6381252241    |
+--------+---------------+
| null   | 2026630299    |
+--------+---------------+
| 3.5    | 1894153540    |
+--------+---------------+

Caveats
=======

In addition to the caveats listed in the background above, Linehaul suffered
from a bug which caused it to significantly under-report download statistics
prior to July 26, 2018. Downloads before this date are proportionally accurate
(e.g. the percentage of Python 2 vs. Python 3 downloads) but total numbers are
lower than actual by an order of magnitude.


Additional tools
================

Besides using the BigQuery console, there are some additional tools which may
be useful when analyzing download statistics.

``google-cloud-bigquery``
-------------------------

You can also access the public PyPI download statistics dataset
programmatically via the BigQuery API and the `google-cloud-bigquery`_ project,
the official Python client library for BigQuery.

.. code-block:: python

    from google.cloud import bigquery

    # Note: depending on where this code is being run, you may require
    # additional authentication. See:
    # https://cloud.google.com/bigquery/docs/authentication/
    client = bigquery.Client()

    query_job = client.query("""
    SELECT COUNT(*) AS num_downloads
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE file.project = 'pytest'
      -- Only query the last 30 days of history
      AND DATE(timestamp)
        BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
        AND CURRENT_DATE()""")

    results = query_job.result()  # Waits for job to complete.
    for row in results:
        print("{} downloads".format(row.num_downloads))


``pypinfo``
-----------

`pypinfo`_ is a command-line tool which provides access to the dataset and
can generate several useful queries. For example, you can query the total
number of download for a package with the command ``pypinfo package_name``.

Install `pypinfo`_ using pip.

.. code-block:: bash

    python -m pip install pypinfo

Usage:

.. code-block:: console

    $ pypinfo requests
    Served from cache: False
    Data processed: 6.87 GiB
    Data billed: 6.87 GiB
    Estimated cost: $0.04

    | download_count |
    | -------------- |
    |      9,316,415 |


``pandas-gbq``
--------------

The `pandas-gbq`_ project allows for accessing query results via `Pandas`_.


References
==========

.. [#] `PyPI Download Counts deprecation email <https://mail.python.org/pipermail/distutils-sig/2013-May/020855.html>`__
.. [#] `PyPI BigQuery dataset announcement email <https://mail.python.org/pipermail/distutils-sig/2016-May/028986.html>`__

.. _public PyPI download statistics dataset: https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=pypi&page=dataset
.. _Google BigQuery: https://cloud.google.com/bigquery
.. _BigQuery web UI: https://console.cloud.google.com/bigquery
.. _pypinfo: https://github.com/ofek/pypinfo/blob/master/README.rst
.. _google-cloud-bigquery: https://cloud.google.com/bigquery/docs/reference/libraries
.. _pandas-gbq: https://pandas-gbq.readthedocs.io/en/latest/
.. _Pandas: https://pandas.pydata.org/
