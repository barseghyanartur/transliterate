#!/usr/bin/env python
import os
import sys


def main():
    sys.path.insert(0, os.path.abspath('src'))
    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    sys.exit(main())
