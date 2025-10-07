# -- Project information ---------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

# Some options are only enabled for the main packaging.python.org deployment builds
RTD_BUILD = bool(os.getenv("READTHEDOCS"))
RTD_PR_BUILD = RTD_BUILD and os.getenv("READTHEDOCS_VERSION_TYPE") == "external"
RTD_URL = os.getenv("READTHEDOCS_CANONICAL_URL")
RTD_CANONICAL_BUILD = (
    RTD_BUILD and not RTD_PR_BUILD and "packaging.python.org" in RTD_URL
)

project = "Python Packaging User Guide"

copyright = "2013–2020, PyPA"
author = "Python Packaging Authority"

# -- General configuration -------------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

root_doc = "index"

extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx_toolbox.collapse",
    "sphinx-jsonschema",
]

nitpicky = True
nitpick_ignore = [
    ("envvar", "PATH"),
    ("py:func", "find_packages"),
    ("py:func", "setup"),
    ("py:func", "importlib.metadata.entry_points"),
    ("py:class", "importlib.metadata.EntryPoint"),
    ("py:func", "setuptools.find_namespace_packages"),
    ("py:func", "setuptools.find_packages"),
    ("py:func", "setuptools.setup"),
]

default_role = "any"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for internationalization --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalization

language = "en"

locale_dirs = ["../locales"]

gettext_auto_build = True
gettext_compact = "messages"
gettext_location = True

# -- Options for HTML output -----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Python Packaging User Guide"
html_theme = "furo"

html_theme_options = {
    "source_edit_link": "https://github.com/pypa/packaging.python.org/edit/main/source/{filename}",
    "source_view_link": "https://github.com/pypa/packaging.python.org/blob/main/source/{filename}?plain=true",
}

html_favicon = "assets/py.png"
html_last_updated_fmt = ""

_metrics_js_files = [
    (
        "https://analytics.python.org/js/script.outbound-links.js",
        {"data-domain": "packaging.python.org", "defer": "defer"},
    ),
]
html_js_files = []
if RTD_CANONICAL_BUILD:
    # Enable collection of the visitor metrics reported at
    # https://plausible.io/packaging.python.org
    html_js_files.extend(_metrics_js_files)

# -- Options for HTML help output ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-help-output

htmlhelp_basename = "pythonpackagingguide-authdoc"

# -- Options for LaTeX output ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {}
latex_documents = [
    (
        root_doc,
        "pythonpackagingguide.tex",
        "Python Packaging User Guide",
        "Python Packaging Authority",
        "manual",
    ),
]

# -- Options for manual page output ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-manual-page-output

man_pages = [
    (root_doc, "pythonpackagingguide", "Python Packaging User Guide", [author], 1)
]

# -- Options for Texinfo output --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-texinfo-output

texinfo_documents = [
    (
        root_doc,
        "pythonpackagingguide",
        "Python Packaging User Guide",
        author,
        "pythonpackagingguide",
        "One line description of project.",
        "Miscellaneous",
    ),
]

# -- Options for the linkcheck builder -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_ignore = [
    r"http://localhost:\d+",
    r"https://packaging\.python\.org/en/latest/specifications/schemas/.*",
    r"https://test\.pypi\.org/project/example-package-YOUR-USERNAME-HERE",
    r"https://pypi\.org/manage/.*",
    r"https://test\.pypi\.org/manage/.*",
    # Temporarily ignored. Ref:
    # https://github.com/pypa/packaging.python.org/pull/1308#issuecomment-1775347690
    r"https://www\.breezy-vcs\.org/.*",
    # Ignore while StackOverflow is blocking GitHub CI. Ref:
    # https://github.com/pypa/packaging.python.org/pull/1474
    r"https://stackoverflow\.com/.*",
    r"https://pyscaffold\.org/.*",
    r"https://anaconda\.org",
    r"https://www\.cisa\.gov/sbom",
    r"https://developers\.redhat\.com/products/softwarecollections/overview",
    r"https://math-atlas\.sourceforge\.net/?",
    r"https://click\.palletsprojects\.com/.*",
    r"https://typer\.tiangolo\.com/.*",
]
linkcheck_retries = 5
# Ignore anchors for common targets when we know they likely won't be found
linkcheck_anchors_ignore_for_url = [
    # GitHub synthesises anchors in JavaScript, so Sphinx can't find them in the HTML
    r"https://github\.com/",
    r"https://docs\.github\.com/",
    # While PyPI has its botscraping defenses active, Sphinx can't resolve the anchors
    # https://github.com/pypa/packaging.python.org/issues/1744
    r"https://pypi\.org/",
]

# -- Options for extlinks ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#configuration

github_url = "https://github.com"
github_repo_org = "pypa"
github_repo_name = "packaging.python.org"
github_repo_slug = f"{github_repo_org}/{github_repo_name}"
github_repo_url = f"{github_url}/{github_repo_slug}"
github_repo_issues_url = f"{github_url}/{github_repo_slug}/issues"
github_sponsors_url = f"{github_url}/sponsors"

extlinks = {
    "issue": (f"{github_repo_issues_url}/%s", "#%s"),
    "pr": (f"{github_repo_url}/pull/%s", "PR #%s"),
    "commit": (f"{github_repo_url}/commit/%s", "%s"),
    "gh": (f"{github_url}/%s", "GitHub: %s"),
    "user": (f"{github_sponsors_url}/%s", "@%s"),
}

# -- Options for intersphinx ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    "boltons": ("https://boltons.readthedocs.io/en/latest/", None),
    "bottle": ("https://bottlepy.org/docs/dev/", None),
    "build": ("https://pypa-build.readthedocs.io/en/stable/", None),
    "cffi": ("https://cffi.readthedocs.io/en/latest/", None),
    "conda": ("https://conda.io/en/latest/", None),
    "devpi": ("https://devpi.net/docs/devpi/devpi/latest/+doc", None),
    "dh-virtualenv": ("https://dh-virtualenv.readthedocs.io/en/latest/", None),
    "distlib": ("https://distlib.readthedocs.io/en/latest/", None),
    "flexx": ("https://flexx.readthedocs.io/en/latest/", None),
    "flit": ("https://flit.pypa.io/en/stable/", None),
    "nox": ("https://nox.thea.codes/en/latest/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "openstack": ("https://docs.openstack.org/glance/latest/", None),
    "packaging": ("https://packaging.pypa.io/en/latest/", None),
    "pip": ("https://pip.pypa.io/en/latest/", None),
    "pipenv": ("https://pipenv.pypa.io/en/latest/", None),
    "piwheels": ("https://piwheels.readthedocs.io/en/latest/", None),
    "pybind11": ("https://pybind11.readthedocs.io/en/stable/", None),
    "pynsist": ("https://pynsist.readthedocs.io/en/latest/", None),
    "pypa": ("https://www.pypa.io/en/latest/", None),
    "python": ("https://docs.python.org/3", None),
    "python-guide": ("https://docs.python-guide.org", None),
    "setuptools": ("https://setuptools.pypa.io/en/latest/", None),
    "spack": ("https://spack.readthedocs.io/en/latest/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "tox": ("https://tox.wiki/en/latest/", None),
    "twine": ("https://twine.readthedocs.io/en/stable/", None),
    "virtualenv": ("https://virtualenv.pypa.io/en/stable/", None),
    "warehouse": ("https://warehouse.pypa.io/", None),
}

# -- Options for todo extension --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for sphinx-copybutton -----------------------------------------------------
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html

copybutton_prompt_text = r">>> |\.\.\. |\$ |> "
copybutton_prompt_is_regexp = True
