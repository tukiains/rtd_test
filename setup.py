
from setuptools import setup, find_packages

setup(
    name='rtd_test',
    version='1.0.0',
    description='Testing with read the docs',
    author='Simo',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.10',
    #install_requires=['netCDF4'],
)
