from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='eztools',
    version='0.0.1',
    description='A tool for Everyday easy use',
    author='Qi Mei',
    author_email='qi.mei@outlook.com',
    packages=find_packages(where='.'),
    include_package_data=True,
)