# Envrio Databases Library

A library to manage the Envrio MySql and Influx databases.

## Modules:

**Module Name: engine**
**version: 1.0.0**

Creates the engine that connects to the MySql database.

**Module Name: models**
**version: 1.0.0**

Creates a MySql database with the tables-columns:
<br>
**user_tables**
*id*, *name*, *email*, *subscription_expires_in*
<br>
**stations**
*id*, *brand*, *model*, *code*, *date_created*,
*longitude*, *latitude*, *elevation*, *access*,
*name*, *icon_type*
**gateways**
*id*, *brand*, *model*, *code*, *name*, *station_id*
**remote_terminal_units**
*id*, *brand*, *model*, *code*, *longitude*, *latitude*,
*elevation*, *name*, *icon_type*
**sensors_meters**
*id*, *type*, *measurement*, *unit*, *gauge_height*,
*name*, *code*, *station_id*, *rtu_id*
**farms_registry**
*id*, *user_id*, *longitude*, *latitude*
**fields_registry**
*id*, *farm_id*, *boundaries*, *soil_properties*
**applications_registry**
*id*, *field_id*, *type*, *status*, *suggested_amount*,
*applied_amount*, *applied_in*
**advices_registry**
*id*, *field_id*, *type*, *status*, *date_registered*, *date_created*
**measurement_translations**
*measurement*
*el*
*en*

**Module Name: schemas**
**version: 1.0.0**

Validates the data type before they are used by crud methods.

**Module Name: crud**
**version: 1.0.0**

Defines all the methods that Create, Read, Update and Delete
tables, rows, etc. from MySql database. It includes the
folloing classes-methods:
**User**
*add*, *get_by_name*, *get_by_id*, *get_by_email*
**Stations**
*add*, *get_by_code*, *get_by_brand*, *get_by_access*, *update_date_created*, *delete_by_code*
**Gateways**
*add*, *get_by_code*
**RemoteTerminalUnits**
*add*, *get_by_code*, *get_by_station_id*
**SensorsMeters**
*add*, *get_by_station_id*, *get_by_rtu_id*, *get_by_station_id_and_rtu_id*, *get_by_id*
**MeasurementsTranslations**
*add*, *get_translation_by_measurement*

**Module Name: influx**
**version: 1.0.1**

Connects to the InfluxDB database and defines all the required 
methods to insert data rows, delete rows, retrive bucket info
and update bucket info. Defines the following methods:
*write_point*, *delete_rows*, *query_data*, *list_buckets*, *update_bucket*

