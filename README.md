# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and InfluxDB databases.

# Documentation

This section contains a link to the library descriptive documentation
+ <a href="https://envrio.org/documentation/databases_library/dl_doc.html">Library Documentation</a>

# Installation

The library is available in GitHub and can be directly installed:<br>

**pipenv**

*pipenv install git+https://github.com/Envrio-hub/databases-utils.git@1.3.0*

**pip**

*pip install git+https://github.com/Envrio-hub/databases-utils.git@1.3.0*

## Latest Release Notes

**Version: 1.3.0**

**Release Date: 2024-10-03**

**Module Name: engine**
<br>
**Version: 1.2.0**

+ Reading the mysql configuration settings from AWS SecretsManager
+ Move the logging_path variable to global variables

**Module Name: models**
<br>
**Version: 1.4.1**

+ Correcting multiple discrepancies between models and MySql actual data base implementation
+ Switch to enum.variables datatype for enum variables

**Module Name: schemas**
<br>
**Version: 1.3.0**

Class: *UsersTable*
+ Multiple corrections to data types

**Module Name: crud**
<br>
**Version: 1.3.0**

Class: *Stations*
+ Adding decorators to handle try except loops
+ Adding decorator to validate given arguments data types
+ Adding a new method named *add_user_to_station*

**Module Name: influx**
<br>
**Version: 1.1.2**

General
+ Add the influx error hndler decorator to handle try except loops

Class: *InfluxConnector*
+ Added database connection status check
