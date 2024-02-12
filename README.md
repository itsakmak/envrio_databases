# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and InfluxDB databases.

# Documentation

This section contains a link to the library descriptive documentation
+ <a href="https://envrio.org/documentation/databases_library/dl_doc.html">Library Documentation</a>

# Installation

The library is available in GitHub and can be directly installed:<br>

**pipenv**

*pipenv install git+https://github.com/Envrio-hub/databases-utils.git@1.2.0*

**pip**

*pip install git+https://github.com/Envrio-hub/databases-utils.git@1.2.0*

## Latest Release Notes

**Version: 1.2.0**

**Release Date: 2024-02-12**

**Module Name: models**
<br>
**Version: 1.3.0**

Table: *stations*
+ Renaming the column *latest_update* to *latest_communication*
+ Adding a new column named *status*

Table: *repeater_units*
+ Adding a new column named *latest_communication*
+ Adding a new column named *status*

Table: *remote_terminal_units*
+ Adding a new column named *latest_communication*
+ Adding a new column named *status*

Table: *monitored_paremeters*
+ Modifing the *device_type* column data type to ENUM('sensor','meter','calculated')
+ Adding a new column named *date_created*
+ Adding a new column named *latest_communication*
+ Adding a new column named *status*

**Module Name: schemas**
<br>
**Version: 1.2.0**

Class: *StationsBase*
+ Renaming the class variable *latest_update* to *latest_communication*
+ Adding a new class variable named *status*
  
Class: *ReapeaterUnitsBase*
+ Addng a new class variable named *latest_communication*
+ Adding a new class variable named *status*

Class: *RemoteTerminalUnitsBase*
+ Addng a new class variable named *latest_communication*
+ Adding a new class variable named *status*

Class: *MonitoredParametersBase*
+ Addng a new class variable named *latest_communication*
+ Adding a new class variable named *status*

**Module Name: crud**
<br>
**Version: 1.2.0**

Class: *Stations*
+ Updating the *add* method
+ Adding a new method named *get_by_id*
+ Adding a new method named *update_status*

Class: *ReapeaterUnits*
+ Updating the *add* method
+ Adding a new method named *get_by_id*
+ Adding a new method named *update_status*

Class: *RemoteTerminalUnits*
+ Updating the *add* method
+ Adding a new method named *get_by_id*
+ Adding a new method named *update_status*

Class: *MonitoredParameters*
+ Updating the *add* method
+ Adding a new method named *get_by_id*
+ Adding a new method named *update_status*

