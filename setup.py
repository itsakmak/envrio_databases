from setuptools import setup, find_packages

setup(
    name='databases_utils',
    version='1.4.0',
    description='A library that enables ENVTIO mysql and influx databases management',
    author='Ioannis Tsakmakis, Nikolaos Kokkos',
    author_email='itsakmak@envrio.org, nkokkos@envrio.org',
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[  
        'sqlalchemy>=2.0.23',
        'pydantic>=2.5.2',
        'influxdb-client>=1.39.0',
        'mysql-connector-python>=9.1.0',
        'python-dotenv>=1.0.1',
        'boto3>=1.35.68'
    ],
    classifiers=[  
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.12',
        'Framework :: Flask',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
