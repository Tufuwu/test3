#!/bin/env python

import fbpic
from setuptools import setup, find_packages

# 读取说明文档
with open('./README.md') as f:
    long_description = f.read()

# 读取依赖项
with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]

setup(
    name='fbpic',
    version=fbpic.__version__,
    description='Spectral, quasi-3D Particle-In-Cell for CPU and GPU',
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer='Remi Lehe',
    maintainer_email='remi.lehe@normalesup.org',
    license='BSD-3-Clause-LBNL',
    packages=find_packages('.'),
    install_requires=install_requires,
    extras_require={
        'test': ["pytest", "more-itertools<6.0.0", "openpmd_viewer"]
    },
    include_package_data=True,
    platforms='any',
    url='http://github.com/fbpic/fbpic',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)