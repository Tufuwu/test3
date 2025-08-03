from distutils.core import setup
from setuptools import setup, find_packages
setup(
    name='Stregsystemet',
    version='0.1',
    author='FIT',
    packages=find_packages(include=["stregsystem*", "kiosk*", "stregreport*", "treo*"]),
    license='THE LIMFJORDS-PORTER-WARE LICENSE',
)
