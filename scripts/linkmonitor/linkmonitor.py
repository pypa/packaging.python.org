# Copyright 2017, PyPA
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license:
#   http://creativecommons.org/licenses/by-sa/3.0.

import argparse
from glob import glob
import io
import os
import sys

from bs4 import BeautifulSoup
import yaml

HERE = os.path.abspath(os.path.dirname(__file__))
INVENTORY_FILENAME = os.path.join(HERE, 'inventory.yaml')
REDIRECTS_FILENAME = os.path.join(HERE, 'redirects.yaml')
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
HTML_DIR = os.path.join(ROOT, 'build', 'html')
IGNORED_FILES = [
    'genindex.html'
]


def find_all_named_anchors(filename):
    links = set()

    with io.open(filename, 'r') as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

        for tag in soup.find_all(id=True):
            anchor = tag['id']
            # Ignore non-named IDs.
            if anchor.startswith('id'):
                continue
            # Ignore index anchors
            if anchor.startswith('index-'):
                continue
            # Ignore searchbox anchors
            if anchor == 'searchbox':
                continue

            href = '{}#{}'.format(filename, anchor)
            links.add(href)

    return links


def find_all_named_anchors_in_files(files):
    links = set()

    for filename in files:
        links.add(filename)
        anchors = find_all_named_anchors(filename)
        links.update(anchors)

    return links


def find_links():
    files = glob('**/*.html', recursive=True)
    files = filter(lambda name: name not in IGNORED_FILES, files)
    return find_all_named_anchors_in_files(files)


def load_inventory():
    if not os.path.exists(INVENTORY_FILENAME):
        return set()
    with io.open(INVENTORY_FILENAME, 'r') as inventory_file:
        return set(yaml.load(inventory_file))


def save_inventory(inventory):
    with io.open(INVENTORY_FILENAME, 'w') as inventory_file:
        yaml.dump(sorted(list(inventory)), inventory_file)


def load_redirects():
    with io.open(REDIRECTS_FILENAME, 'r') as redirects_file:
        return yaml.load(redirects_file)


def expand_redirects(redirects, inventory):
    valid_redirects = set()
    missing_redirects = set()

    for redirect in redirects:
        from_ = redirect['from']
        source_links = set()

        # Get all links that start with the page. This gathers all deep links.
        # For example, the redirect may be old.html -> new.html. old.html may
        # have had #1, #2, #3. We need to get all of those deep links.
        for link in inventory:
            if link.startswith(from_):
                source_links.add(link)

        # Make sure all of the source links have a counterpart in the
        # destination page. For the example above, new.html needs to have #1
        # #2 and #3 as well.
        for source_link in source_links:
            dest_link = source_link.replace(from_, redirect['to'])
            if dest_link in inventory:
                valid_redirects.add(source_link)
            else:
                missing_redirects.add((source_link, dest_link))

    return valid_redirects, missing_redirects


def update_command(args):
    """Updates the current inventory of links with any new links added.

    This should be run after adding new documentation to make a record of new
    items added.
    """
    os.chdir(HTML_DIR)

    inventory = load_inventory()
    links = find_links()

    new_links = links.difference(inventory)
    print('Found {} new links.'.format(len(new_links)))

    inventory.update(links)
    save_inventory(inventory)

    return 0


def check_command(args):
    """Checks the current set of links against the inventory.

    This should be run on every documentation change to ensure that no deep
    links have been broken and that new links are tracked in the inventory.
    """
    os.chdir(HTML_DIR)

    # TODO: Add another file to list currently defined redirects.
    inventory = load_inventory()
    redirects = load_redirects()
    links = find_links()

    valid_redirects, missing_redirects = expand_redirects(redirects, inventory)
    if missing_redirects:
        print(
            'The following redirects are missing deep link anchors in the '
            'destination:')
        for source, dest in missing_redirects:
            print(' * {} -> {}'.format(source, dest))

    missing_links = inventory.difference(links)
    missing_links -= valid_redirects

    if missing_links:
        print('Missing the following deep links:')
        for link in missing_links:
            print(' * {}'.format(link))
        return 1

    new_links = links.difference(inventory)

    if new_links:
        print('The following new deep links were added:')
        for link in new_links:
            print(' * {}'.format(link))
        print('Run nox -s updatelinks to update them in git.')
        return 2

    print('All is well')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    update_parser = subparsers.add_parser(
        'update', help=update_command.__doc__)
    update_parser.set_defaults(func=update_command)
    check_parser = subparsers.add_parser(
        'check', help=check_command.__doc__)
    check_parser.set_defaults(func=check_command)

    args = parser.parse_args()

    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)

    sys.exit(args.func(args))
