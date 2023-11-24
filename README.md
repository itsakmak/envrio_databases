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
      <th>Data Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">user_tables</td>
      <td>id</td>
      <td int>
    </tr>
    <tr>
      <td>name</td>
      <td varchar(500)>
    </tr>
    <tr>
      <td>email</td>
      <td varchar(500)>
    </tr>
    <tr>
      <td>email</td>
      <td varchar(500)>
    </tr>
    <tr>
      <td>subscription_expires_in</td>
      <td varchar(20)>
    </tr>
    <tr>
      <td rowspan="11">stations</td>
      <td>id</td>
      <td>int</td>
    </tr>
    <tr>
       <td>brand</td>
       <td>varchar(50)</td>
    </tr>
    <tr>
       <td>model</td>
       <td>varchar(200)</td>
    </tr>
    <tr>
       <td>code</td>
       <td>varchar(100)</td>
    </tr>
    <tr>
       <td>date_created</td>
       <td>varchar(24)</td>
    </tr>
    <tr>
       <td>longitude</td>
       <td>decimal(10,8)</td>
    </tr>
    <tr>
       <td>latitude</td>
       <td>decimal(10,8)</td>
    </tr>
    <tr>
       <td>elevation</td>
       <td>int</td>
    </tr>
    <tr>
       <td>access</td>
       <td>json</td>
    </tr>
    <tr>
       <td>name</td>
       <td>json</td>
    </tr>
    <tr>
       <td>icon_type</td>
       <td>varchar(10)</td>
    </tr>
    <tr>
      <td rowspan="6">gateways</td>
      <td>*id*, *brand*, *model*, *code*, *name*, *station_id*</td>
      <td>int</td>
    </tr>
    <tr>
      <td>brand</td>
      <td>varchar(50)</td>
    </tr>
    <tr>
      <td>model</td>
      <td>varchar(200)</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(500)</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
    </tr>
    <tr>
      <td rowspan="9">remote_terminal_units</td>
      <td>id</td>
      <td>int</td>
    </tr>
    <tr>
      <td>brand</td>
      <td>varchar(50)</td>
    </tr>
    <tr>
      <td>model</td>
      <td>varchar(200)</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>decimal(10,8)</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>decimal(10,8)</td>
    </tr>
    <tr>
      <td>elevation</td>
      <td>int</td>
    </tr>
    <tr>
      <td>name</td>
      <td>json</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
    </tr>
    <tr>
      <td rowspawn="9">sensors_meters</td>
      <td>id</td>
      <td>int</td>
    </tr>
    <tr>
      <td>type</td>
      <td>varchar(7)</td>
    </tr>
    <tr>
      <td>measurement</td>
      <td>varchar(100)</td>
    </tr>
    <tr>
      <td>unit</td>
      <td>varchar(20)</td>
    </tr>
    <tr>
      <td>gauge_height</td>
      <td>float</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(100)</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
    </tr>
    <tr>
      <td>rtu_id</td>
      <td>int</td>
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
Methods: <cite>add, get_by_name, get_by_id, get_by_email</cite>
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

<style>
  cite {
    font-style: italic;
  }
</style>
