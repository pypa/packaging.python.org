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
        yaml.dump(list(inventory), inventory_file)


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
    links have been broken.
    """
    os.chdir(HTML_DIR)

    # TODO: Add another file to list currently defined redirects.
    inventory = load_inventory()
    links = find_links()

    missing_links = inventory.difference(links)

    if not missing_links:
        print('All is well')
        return 0

    print('Missing the following deep links:')
    for link in missing_links:
        print(' * {}'.format(link))

    return 1


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
