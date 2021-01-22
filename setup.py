
from setuptools import setup, find_packages

setup(
    name='rtd_test',
    version='1.0.0',
    description='Testing with netcdf4 and read the docs',
    author='Simo',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    setup_requires=['wheel'],
    install_requires=['netCDF4'],
)
