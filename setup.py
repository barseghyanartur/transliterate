import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'readme.rst')).read()
except:
    readme = ''

version = '1.1'

setup(
    name = 'transliterate',
    version = version,
    description = ("Bi-directional transliterator for Python"),
    long_description=readme,
    classifiers = [
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = 'translit, transliteration',
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://bitbucket.org/barseghyanartur/transliterate',
    package_dir={'':'src'},
    packages=find_packages(where='./src'),
    license='GPL 2.0/LGPL 2.1',
    install_requires=['lorem-ipsum-generator==0.3',]
)
