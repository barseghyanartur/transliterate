import sys
import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

version = '1.9'

install_requires = [
    'six>=1.1.0'
]

try:
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3
    if PY2:
        install_requires.append('lorem-ipsum-generator==0.3')
except:
    pass

setup(
    name='transliterate',
    version=version,
    description="Bi-directional transliterator for Python",
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        # "Natural Language :: Armenian",
        # "Natural Language :: Georgian",
        "Natural Language :: Greek",
        "Natural Language :: Russian",
        "Natural Language :: Ukranian",
    ],
    keywords='translit, transliteration',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/transliterate',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL 2.0/LGPL 2.1',
    install_requires=install_requires
)
