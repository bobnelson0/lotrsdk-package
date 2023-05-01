"""
LOTR SDK setup.py
"""
from setuptools import setup, find_packages

NAME = 'lotrsdk'
VERSION = '1.0.0'
DESCRIPTION = 'Python SDK for interacting with The One Ring API'
AUTHOR = 'Robert (Bobby) Nelson'
AUTHOR_EMAIL = 'bob.nelson@gmail.com'
LICENSE = 'MIT'
REQUIRES = ['requests >= 2.29.0']

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url="https://github.com/bobnelson0/lotrsdk-package",
    packages=find_packages(),
    include_package_data=True,
    license=LICENSE,
    long_description=DESCRIPTION,
    setup_requires=['wheel'],
    install_requires=REQUIRES,
    python_requires='>=3.9'
)
