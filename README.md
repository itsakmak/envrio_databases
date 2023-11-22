# Envrio Databases Library

A library to manage the Envrio MySql and Influx databases.

## Modules:

**Module Name: engine**
<br>
**Version: 1.0.2**

Creates the engine that connects to the MySql database.

**Module Name: models**
<br>
**Version: 1.0.0**

Creates a MySql database with the tables-columns:
<br>
<br>
Name: user_tables
<br>
Columns: *id*, *name*, *email*, *subscription_expires_in*
<br>
<br>
Name: stations
<br>
Columns: *id*, *brand*, *model*, *code*, *date_created*,
*longitude*, *latitude*, *elevation*, *access*,
*name*, *icon_type*
<br>
<br>
Name: gateways
<br>
Columns: *id*, *brand*, *model*, *code*, *name*, *station_id*
<br>
<br>
Name: remote_terminal_units
<br>
Columns: *id*, *brand*, *model*, *code*, *longitude*, *latitude*,
*elevation*, *name*, *icon_type*
<br>
<br>
Name: sensors_meters
<br>
Columns: *id*, *type*, *measurement*, *unit*, *gauge_height*,
*name*, *code*, *station_id*, *rtu_id*
<br>
<br>
Name: farms_registry
<br>
Columns: *id*, *user_id*, *longitude*, *latitude*
<br>
<br>
Name: fields_registry
<br>
Columns: *id*, *farm_id*, *boundaries*, *soil_properties*
<br>
<br>
Name: applications_registry
<br>
Columns: *id*, *field_id*, *type*, *status*, *suggested_amount*,
*applied_amount*, *applied_in*
<br>
<br>
Name: advices_registry
<br>
Columns: *id*, *field_id*, *type*, *status*, *date_registered*, *date_created*
<br>
<br>
Name: measurement_translations
<br>
Columns: *measurement*, *el*, *en*

**Module Name: schemas**
<br>
**Version: 1.0.0**

Validates the data type before they are used by crud methods.

**Module Name: crud**
<br>
**Version: 1.0.0**

Defines all the methods that Create, Read, Update and Delete
tables, rows, etc. from MySql database. It includes the
folloing classes-methods:
<br>
<br>
Class: User
<br>
Methods: *add*, *get_by_name*, *get_by_id*, *get_by_email*
<br>
<br>
Class: Stations
<br>
Methods: *add*, *get_by_code*, *get_by_brand*, *get_by_access*, *update_date_created*, *delete_by_code*
<br>
<br>
Class: Gateways
<br>
Methods: *add*, *get_by_code*
<br>
<br>
Class: RemoteTerminalUnits
<br>
Methods: *add*, *get_by_code*, *get_by_station_id*
<br>
<br>
Class: SensorsMeters
<br>
Methods: *add*, *get_by_station_id*, *get_by_rtu_id*, *get_by_station_id_and_rtu_id*, *get_by_id*
<br>
<br>
**Class:** MeasurementsTranslations
<br>
Methods: *add*, *get_translation_by_measurement*

**Module Name: influx**
<br>
**version: 1.0.1**

Connects to the InfluxDB database and defines all the required 
methods to insert data rows, delete rows, retrive bucket info
and update bucket info. Defines the following methods:
<br>
<br>
Methods: *write_point*, *delete_rows*, *query_data*, *list_buckets*, *update_bucket*

