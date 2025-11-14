import os
import pathlib
import urllib

import sphinx.application
import sphinx.util.logging


DOMAIN = "packaging.python.org"


logger = sphinx.util.logging.getLogger(__name__)


def resolve_local_html_link(app: sphinx.application.Sphinx, url_path: str) -> str:
    """Takes path of a link pointing an HTML render of the current project,
    and returns local path of the referenced document.

    Support links to renders from both the `html` and `dirhtml` builders.

    Example:

    .. code-block:: python

        >>> resolve_local_html_link('https://packaging.python.org/en/latest/flow/')
        '{srcdir}/flow.rst'
        >>> resolve_local_html_link('https://packaging.python.org/en/latest/flow.html')
        '{srcdir}/flow.rst'
        >>> resolve_local_html_link('https://packaging.python.org/en/latest/specifications/schemas/')
        '{srcdir}/specifications/schemas/index.rst'
        >>> resolve_local_html_link('https://packaging.python.org/en/latest/specifications/schemas/build-details-v1.0.schema.json')
        '{html_extra_path0}/specifications/schemas/build-details-v1.0.schema.json'

    """
    # Search for document in html_extra_path
    for entry in app.config.html_extra_path:
        candidate = (app.confdir / entry / url_path).resolve()
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if candidate.exists():
            return os.fspath(candidate)
    # Convert html path to source path
    url_path = url_path.removesuffix("/")  # Normalize
    if url_path.endswith(".html"):
        document = url_path.removesuffix(".html")
    elif (candidate := f"{url_path}/index") in app.project.docnames:
        document = candidate
    else:
        document = url_path
    return app.env.doc2path(document)


def rewrite_local_uri(app: sphinx.application.Sphinx, uri: str) -> str:
    """Replace remote URIs targeting https://packaging.python.org/en/latest/...
    with local ones, so that local changes are taken into account by linkcheck.

    Additionally, resolve local relative links to html_extra_path.
    """
    local_uri = uri
    parsed = urllib.parse.urlparse(uri)
    # Links to https://packaging.python.org/en/latest/...
    if parsed.hostname == DOMAIN and parsed.path.startswith("/en/latest/"):
        document = parsed.path.removeprefix("/en/latest/")
        local_uri = resolve_local_html_link(app, document)
        logger.verbose(
            f"{uri!s} is a remote URL that points to local sources, "
            "replacing it with a local URL in linkcheck to take new changes "
            "into account (pass -vv for more info)"
        )
        logger.debug(f"Replacing linkcheck URL {uri!r} with {local_uri!r}")
    # Local relative links
    if not parsed.scheme and not parsed.netloc and parsed.path:
        full_path = pathlib.Path(app.env.docname).parent / parsed.path
        local_uri = resolve_local_html_link(app, os.fspath(full_path))
        if local_uri != uri:
            logger.verbose(f"Local linkcheck URL {uri!r} resolved as {local_uri!r}")
    return local_uri


def setup(app: sphinx.application.Sphinx) -> dict[str, bool]:
    app.connect("linkcheck-process-uri", rewrite_local_uri)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
