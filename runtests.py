#!/usr/bin/env python
import os
import sys

import pytest


def main():
    sys.path.insert(0, os.path.abspath('src'))
    return pytest.main()


if __name__ == '__main__':
    sys.exit(main())
