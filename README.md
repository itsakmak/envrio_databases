# Envrio Databases Library

A library to manage the Envrio MySql and Influx databases.

## Modules:

**Module Name: engine**
<br>
**Version: 1.0.4**

Creates the engine that connects to the MySql database.

**Module Name: models**
<br>
**Version: 1.0.2**

Creates a MySql database with the tables-columns shown in the 
following table:
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Table Names</th>
      <th>Column Names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>user_tables</td>
      <td>*id*, *name*, *email*, *subscription_expires_in*</td>
    </tr>
    <tr>
      <td>stations</td>
      <td>*id*, *brand*, *model*, *code*, *date_created*,
         *longitude*, *latitude*, *elevation*, *access*,
            *name*, *icon_type*</td>
    </tr>
    <tr>
      <td>gateways</td>
      <td>*id*, *brand*, *model*, *code*, *name*, *station_id*</td>
    </tr>
    <tr>
      <td>remote_terminal_units</td>
      <td>*id*, *brand*, *model*, *code*, *longitude*, *latitude*,
            *elevation*, *name*, *icon_type*</td>
    </tr>
    <tr>
      <td>sensors_meters</td>
      <td>*id*, *type*, *measurement*, *unit*, *gauge_height*,
            *name*, *code*, *station_id*, *rtu_id*</td>
    </tr>
    <tr>
      <td>farms_registry</td>
      <td>*id*, *user_id*, *longitude*, *latitude*</td>
    </tr>
    <tr>
      <td>fields_registry</td>
      <td>*id*, *farm_id*, *boundaries*, *soil_properties*</td>
    </tr>
    <tr>
      <td>applications_registry</td>
      <td>*id*, *field_id*, *type*, *status*, *suggested_amount*,
            *applied_amount*, *applied_in*</td>
    </tr>
    <tr>
      <td>advices_registry</td>
      <td>*id*, *field_id*, *type*, *status*, *date_registered*, *date_created*</td>
    </tr>
    <tr>
      <td>measurement_translations</td>
      <td>*measurement*, *el*, *en*</td>
    </tr>
  </tbody>
</table>

**Module Name: schemas**
<br>
**Version: 1.0.0**

Validates the data type before they are used by crud methods.

**Module Name: crud**
<br>
**Version: 1.0.2**

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

