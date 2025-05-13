from __future__ import absolute_import, division, print_function

from setuptools import setup, find_packages

setup(
    name='amazon.ion',
    version='0.7.0',
    description='A Python implementation of Amazon Ion.',
    url='http://github.com/amzn/ion-python',
    author='Amazon Ion Team',
    author_email='ion-team@amazon.com',
    license='Apache License 2.0',

    packages=find_packages(exclude=['tests*']),
    namespace_packages=['amazon'],

    install_requires=[
        'six',
        'jsonconversion'
    ],

    extras_require={
        'dev': ['pytest'],
    },

    python_requires='>=3.6',
)