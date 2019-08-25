================================
Analyzing PyPI package downloads
================================

This section covers how to use the `PyPI package dataset`_ to learn more
about downloads of a package (or packages) hosted on PyPI. For example, you can
use it to discover the distribution of Python versions used to download a
package.

.. contents:: Contents
   :local:


Background
==========

PyPI does not display download statistics because they are difficult to
collect and display accurately. Reasons for this are included in the
`announcement email
<https://mail.python.org/pipermail/distutils-sig/2013-May/020855.html>`__:

    There are numerous reasons for [download counts] removal/deprecation some
    of which are:

        - Technically hard to make work with the new CDN

            - The CDN is being donated to the PSF, and the donated tier does
              not offer any form of log access
            - The work around for not having log access would greatly reduce
              the utility of the CDN
        - Highly inaccurate
            - A number of things prevent the download counts from being
              accurate, some of which include:

                - pip download cache
                - Internal or unofficial mirrors
                - Packages not hosted on PyPI (for comparisons sake)
                - Mirrors or unofficial grab scripts causing inflated counts
                  (Last I looked 25% of the downloads were from a known
                  mirroring script).
        - Not particularly useful

            - Just because a project has been downloaded a lot doesn't mean
              it's good
            - Similarly just because a project hasn't been downloaded a lot
              doesn't mean it's bad

    In short because it's value is low for various reasons, and the tradeoffs
    required to make it work are high It has been not an effective use of
    resources.

As an alternative, the `Linehaul project
<https://github.com/pypa/linehaul>`__ streams download logs to `Google
BigQuery`_ [#]_. Linehaul writes an entry in a
``the-psf.pypi.downloadsYYYYMMDD`` table for each download. The table
contains information about what file was downloaded and how it was
downloaded. Some useful columns from the `table schema
<https://bigquery.cloud.google.com/table/the-psf:pypi.downloads20161022?tab=schema>`__
include:

+------------------------+-----------------+-----------------------+
| Column                 | Description     | Examples              |
+========================+=================+=======================+
| file.project           | Project name    | ``pipenv``, ``nose``  |
+------------------------+-----------------+-----------------------+
| file.version           | Package version | ``0.1.6``, ``1.4.2``  |
+------------------------+-----------------+-----------------------+
| details.installer.name | Installer       | pip, `bandersnatch`_  |
+------------------------+-----------------+-----------------------+
| details.python         | Python version  | ``2.7.12``, ``3.6.4`` |
+------------------------+-----------------+-----------------------+

.. [#] `PyPI BigQuery dataset announcement email <https://mail.python.org/pipermail/distutils-sig/2016-May/028986.html>`__

Setting up
==========

In order to use `Google BigQuery`_ to query the `PyPI package dataset`_,
you'll need a Google account and to enable the BigQuery API on a Google
Cloud Platform project. You can run the up to 1TB of queries per month `using
the BigQuery free tier without a credit card
<https://cloud.google.com/blog/big-data/2017/01/how-to-run-a-terabyte-of-google-bigquery-queries-each-month-without-a-credit-card>`__

- Navigate to the `BigQuery web UI`_.
- Create a new project.
- Enable the `BigQuery API
  <https://console.developers.google.com/apis/library/bigquery-json.googleapis.com>`__.

For more detailed instructions on how to get started with BigQuery, check out
the `BigQuery quickstart guide
<https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui>`__.

Useful queries
==============

Run queries in the `BigQuery web UI`_ by clicking the "Compose query" button.

Note that the rows are stored in separate tables for each day, which helps
limit the cost of queries. These example queries analyze downloads from
recent history by using `wildcard tables
<https://cloud.google.com/bigquery/docs/querying-wildcard-tables>`__ to
select all tables and then filter by ``_TABLE_SUFFIX``.

Counting package downloads
--------------------------

The following query counts the total number of downloads for the project
"pytest".

::

    #standardSQL
    SELECT COUNT(*) AS num_downloads
    FROM `the-psf.pypi.downloads*`
    WHERE file.project = 'pytest'
      -- Only query the last 30 days of history
      AND _TABLE_SUFFIX
        BETWEEN FORMAT_DATE(
          '%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
        AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())

+---------------+
| num_downloads |
+===============+
| 2117807       |
+---------------+

To only count downloads from pip, filter on the ``details.installer.name``
column.

::

    #standardSQL
    SELECT COUNT(*) AS num_downloads
    FROM `the-psf.pypi.downloads*`
    WHERE file.project = 'pytest'
      AND details.installer.name = 'pip'
      -- Only query the last 30 days of history
      AND _TABLE_SUFFIX
        BETWEEN FORMAT_DATE(
          '%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
        AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())

+---------------+
| num_downloads |
+===============+
| 1829322       |
+---------------+

Package downloads over time
---------------------------

To group by monthly downloads, use the ``_TABLE_SUFFIX`` pseudo-column. Also
use the pseudo-column to limit the tables queried and the corresponding
costs.

::

    #standardSQL
    SELECT
      COUNT(*) AS num_downloads,
      SUBSTR(_TABLE_SUFFIX, 1, 6) AS `month`
    FROM `the-psf.pypi.downloads*`
    WHERE
      file.project = 'pytest'
      -- Only query the last 6 months of history
      AND _TABLE_SUFFIX
        BETWEEN FORMAT_DATE(
          '%Y%m01', DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH))
        AND FORMAT_DATE('%Y%m%d', CURRENT_DATE())
    GROUP BY `month`
    ORDER BY `month` DESC

+---------------+--------+
| num_downloads | month  |
+===============+========+
| 1956741       | 201801 |
+---------------+--------+
| 2344692       | 201712 |
+---------------+--------+
| 1730398       | 201711 |
+---------------+--------+
| 2047310       | 201710 |
+---------------+--------+
| 1744443       | 201709 |
+---------------+--------+
| 1916952       | 201708 |
+---------------+--------+

More queries
------------

- `Data driven decisions using PyPI download statistics
  <https://langui.sh/2016/12/09/data-driven-decisions/>`__
- `PyPI queries gist <https://gist.github.com/alex/4f100a9592b05e9b4d63>`__
- `Python versions over time
  <https://github.com/tswast/code-snippets/blob/master/2018/python-community-insights/Python%20Community%20Insights.ipynb>`__
- `Non-Windows downloads, grouped by platform
  <https://bigquery.cloud.google.com/savedquery/51422494423:ff1976af63614ad4a1258d8821dd7785>`__

Additional tools
================

You can also access the `PyPI package dataset`_ programmatically via the
BigQuery API.

pypinfo
-------

`pypinfo`_ is a command-line tool which provides access to the dataset and
can generate several useful queries. For example, you can query the total
number of download for a package with the command ``pypinfo package_name``.

::

    $ pypinfo requests
    Served from cache: False
    Data processed: 6.87 GiB
    Data billed: 6.87 GiB
    Estimated cost: $0.04

    | download_count |
    | -------------- |
    |      9,316,415 |

Install `pypinfo`_ using pip.

::

    pip install pypinfo

Other libraries
---------------

- `google-cloud-bigquery`_ is the official client library to access the
  BigQuery API.
- `pandas-gbq`_ allows for accessing query results via `Pandas`_.

.. _PyPI package dataset: https://bigquery.cloud.google.com/dataset/the-psf:pypi
.. _bandersnatch: /key_projects/#bandersnatch
.. _Google BigQuery: https://cloud.google.com/bigquery
.. _BigQuery web UI: https://console.cloud.google.com/bigquery
.. _pypinfo: https://github.com/ofek/pypinfo/blob/master/README.rst
.. _google-cloud-bigquery: https://cloud.google.com/bigquery/docs/reference/libraries
.. _pandas-gbq: https://pandas-gbq.readthedocs.io/en/latest/
.. _Pandas: https://pandas.pydata.org/
