# -*- coding: utf-8 -*-

import argparse
import sys

from hey_officer.core import Checker


def _create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*', help='Paths to check')
    return parser


def main():
    parser = _create_parser()
    args = parser.parse_args()

    Checker(args.paths).run()


if __name__ == '__main__':
    main()
