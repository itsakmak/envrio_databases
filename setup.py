from setuptools import setup, find_packages

setup(
    name='databases_library',
    version='1.0.1',
    description='A library that enables ENVTIO mysql and influx databases management',
    author='Ioannis Tsakmakis, Nikolaos Kokkos',
    author_email='itsakmak@envrio.org, nkokkos@envrio.org',
    packages=find_packages(),
    python_requires='>=3.12'
)
