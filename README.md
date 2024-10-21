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

**Release Date: 2024-10-15**

**Module Name: engine**
<br>
**Version: 1.2.0**

+ Reading the mysql configuration settings from AWS SecretsManager
+ Move the logging_path variable to global variables

**Module Name: models**
<br>
**Version: 1.4.4**

*General*
+ Adding a new class MetricaApiCredentials
+ Adding a new class ADCONApiCredentials

*MonitoredParameters*
+ Changed name column from str to JSON

**Module Name: schemas**
<br>
**Version: 1.3.2**

*General*
+ Adding a new class MetricaApiCredentialsBase
+ Addin a new class ADCONApiCredentialsBase


**Module Name: crud**
<br>
**Version: 1.3.6**

*General*
+ Adding a new class MetricaApiCredentials
+ Adding a new class ADCONApiCredentials
+ 
*MonitoredParameters*
+ Adding a new method update_status_by_station_id
+ Adding a new method update_last_communication_by_station_id

**Module Name: influx**
<br>
**Version: 1.1.3**

*General*
+ Replacing the alchemy logger handler with the influxdb handler
