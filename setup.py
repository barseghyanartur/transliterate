import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '1.11'

install_requires = [
    'six>=1.1.0'
]

tests_require = [
    'factory_boy',
    'faker',
    'pytest',
    'pytest-cov',
    'tox'
]

setup(
    name='transliterate',
    version=version,
    description="Bi-directional transliterator for Python",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        # "Natural Language :: Armenian",
        # "Natural Language :: Georgian",
        "Natural Language :: Bulgarian",
        "Natural Language :: Greek",
        "Natural Language :: Macedonian",
        "Natural Language :: Russian",
        "Natural Language :: Serbian",
        "Natural Language :: Ukrainian",
        "Natural Language :: Uzbek",
    ],
    keywords='translit, transliteration',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/transliterate',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL-2.0-only OR LGPL-2.1-or-later',
    install_requires=install_requires,
    tests_require=tests_require,
    include_package_data=True,
)
