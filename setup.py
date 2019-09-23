import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="synonymfinder",

    description="Finds synonyms for jobs",

    author="Andrew Sutjahjo",

    packages=find_packages(exclude=['results', 'data']),

    long_description=read('README.md'),
)