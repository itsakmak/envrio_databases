# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and InfluxDB databases.

# Documentation

This section contains a link to the library descriptive documentation
+ <a href="https://envrio.org/documentation/databases_library/dl_doc.html">Library Documentation</a>

# Installation

The library is available in GitHub and can be directly installed:<br>

**pipenv**

*pipenv install git+https://github.com/Envrio-hub/databases-utils.git@1.2.1*

**pip**

*pip install git+https://github.com/Envrio-hub/databases-utils.git@1.2.1*

## Latest Release Notes

**Version: 1.2.1**

**Release Date: 2024-09-20**

**Module Name: models**
<br>
**Version: 1.3.2**

Table: *users_table*
+ Adding a new column named *account_type*

**Module Name: schemas**
<br>
**Version: 1.2.2**

Class: *UsersTable*
+ Adding a new class variable named *account_type*

**Module Name: crud**
<br>
**Version: 1.2.2**

Class: *Stations*
+ Adding a new method named *delete_user_from_station*
+ Adding a new method named *add_user_to_station*