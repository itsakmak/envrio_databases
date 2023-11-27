# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and Influx databases.

## Modules:

**Module Name: engine**
<br>
**Version: 1.0.5**

Creates the engine that connects an app to the MySql database.

**Module Name: models**
<br>
**Version: 1.0.4**

Creates the envrio_core MySql database with the tables-columns shown in the 
following table:
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Table Name</th>
      <th>Column Name</th>
      <th>Data Type</th>
      <th>Short Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">user_tables</td>
      <td>id</td>
      <td>int</td>
      <td>User unique indentification number</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(500)</td>
      <td>User cognito name</td>
    </tr>
    <tr>
      <td>email</td>
      <td>varchar(500)</td>
      <td>User email</td>
    </tr>
    <tr>
      <td>subscription_expires_in</td>
      <td>float</td>
      <td>The timestampt that the user subscription expires</td>
    </tr>
    <tr>
      <td rowspan="11">stations</td>
      <td>id</td>
      <td>int</td>
      <td>Station unique identification number</td>
    </tr>
    <tr>
       <td>brand</td>
       <td>varchar(50)</td>
       <td>Station brand</td>
    </tr>
    <tr>
       <td>model</td>
       <td>varchar(200)</td>
       <td>Station specific model</td>
    </tr>
    <tr>
       <td>code</td>
       <td>varchar(100)</td>
       <td>Station id as defined in the data providers API</td>
    </tr>
    <tr>
       <td>date_created</td>
       <td>float</td>
       <td>The timestamp that station installed on the field and started to transmit data</td>
    </tr>
    <tr>
       <td>longitude</td>
       <td>decimal(10,8)</td>
       <td>The lognitude of the station's installation point</td>
    </tr>
    <tr>
       <td>latitude</td>
       <td>decimal(10,8)</td>
        <td>The latitude of the station's installation point</td>
    </tr>
    <tr>
       <td>elevation</td>
       <td>int</td>
       <td>The elevation of the station's installation point</td>
    </tr>
    <tr>
       <td>access</td>
       <td>json</td>
       <td>A json object that contains an array with the user_ids that have an active subscription for the station e.g. {"users": [1,2,3]}</td>
    </tr>
    <tr>
       <td>name</td>
       <td>json</td>
       <td>A json object with the name that is give to the station is various languages e.g., {"el":"Αθήνα","en":"Athens"}.
       Usually the name of the station corresponds to the location that it is installed</td>
    </tr>
    <tr>
       <td>icon_type</td>
       <td>varchar(10)</td>
       <td>The type of the station. It can be on of 'meteo', 'coastal' or 'hydro'</td>
    </tr>
    <tr>
      <td rowspan="6">gateways</td>
      <td>id</td>
      <td>int</td>
      <td>Gatewasy unique identification number</td>
    </tr>
    <tr>
      <td>brand</td>
      <td>varchar(50)</td>
      <td>Gateway brand</td>
    </tr>
    <tr>
      <td>model</td>
      <td>varchar(200)</td>
      <td>Gateway specific model</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
      <td>Gateway id as defined in the data providers API</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(500)</td>
      <td>Gateway name as defined in the data provider API</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
      <td>The id of the station that the gateways is connected to</td>
    </tr>
    <tr>
      <td rowspan="9">remote_terminal_units</td>
      <td>id</td>
      <td>int</td>
      <td>remote terminal unit unique identification number</td>
    </tr>
    <tr>
      <td>brand</td>
      <td>varchar(50)</td>
      <td>remote terminal unit brand</td>
    </tr>
    <tr>
      <td>model</td>
      <td>varchar(200)</td>
      <td>remote terminal unit specific model</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
      <td>remote terminal unit id as defined in the data providers API</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>decimal(10,8)</td>
      <td>The longitude of the remote terminal unit's installation point</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>decimal(10,8)</td>
      <td>The latitude of the remote terminal unit's installation point</td>
    </tr>
    <tr>
      <td>elevation</td>
      <td>int</td>
      <td>The elevation of the remote terminal unit's installation point</td>
    </tr>
    <tr>
      <td>name</td>
      <td>json</td>
       <td>A json object with the name that is give to the remote terminal unit is various languages e.g., {"el":"Τερματική Μονάδα 1","en":"Terminal Unit 1"}</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
      <td>The id of the station that the remote terminal unit is paired with</td>
    </tr>
    <tr>
      <td rowspan="9">sensors_meters</td>
      <td>id</td>
      <td>int</td>
      <td>Sensor or Meter unique identification number</td>
    </tr>
    <tr>
      <td>type</td>
      <td>varchar(7)</td>
      <td>Can be one of 'sensor', 'meter', or 'calc' if it's a value calculated based on a formula</td>
    </tr>
    <tr>
      <td>measurement</td>
      <td>varchar(100)</td>
      <td>The name of the parameter that is measured. The nomenclature is mainly based on the <a href="https://cfconventions.org/Data/cf-standard-names/29/build/cf-standard-name-table.html">CF Standard Names<a></td>
    </tr>
    <tr>
      <td>unit</td>
      <td>varchar(20)</td>
      <td>The unit that the measurements are reported</td>
    </tr>
    <tr>
      <td>gauge_height</td>
      <td>float</td>
      <td>The height (m) that the sensor-meter is placed in reference to the surface. If the sensor-meter is installed within 
      the soil or into the sea the gauge_height gets negative values</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(100)</td>
      <td>Sensor-meter name as defined in the data provider API</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
      <td>Sensor-meter id as defined in the data provider API</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
      <td>The id of the station that the sensor-meter is connected to</td>
    </tr>
    <tr>
      <td>rtu_id</td>
      <td>int</td>
      <td>The id of the remote terminal unit that the sensor-meter is connected to</td>
    </tr>
    <tr>
      <td rowspan="4">farms_registry</td>
      <td>id</td>
      <td>int</td>
      <td>A farm unique identification number</td>
    </tr>
    <tr>
      <td>user_id</td>
      <td>int</td>
      <td>The user id that the farm belong's to</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>decimal(10,8)</td>
      <td>The longitude of the farm location</td>
    </tr>
    <tr>
      <td>latitude</td>
      <td>decimal(10,8)</td>
      <td>The latitude of the farm location</td>
    </tr>
    <tr>
      <td rowspan="4">fields_registry</td>
      <td>A field unique identification number</td>
      <td>id</td>
      <td>int</td>
    </tr>
    <tr>
      <td>farm_id</td>
      <td>int</td>
      <td>The farm id that the farm is assigned to</td>
    </tr>
    <tr>
      <td>boundaries</td>
      <td>json</td>
      <td>A <a href="https://geojson.org/">GeoJSON</a> with the field boundaries</td>
    </tr>
    <tr>
      <td>soil_properties</td>
      <td>json</td>
      <td>A json object that includes the key layers that refers to the field distict soil layers and the key data that it's an array with the hydraulic properties (sat=saturation point,fc=field capacit,pwp=permanent wilting poin,ksat=saturated hydraulic conductivity) for each layer e.g., {"layers":2,"data":[{"depth":5,"sat":40,"fc":32,"pwp":14,"ksat":100},{"depth":25,"sat":42,"fc":35,"pwp":15,"ksat":100}]}</td>
    </tr>
    <tr>
      <td rowspan="6">applications_registry</td>
      <td>id</td>
      <td>int</td>
      <td>An application unique identification number</td>
    </tr>
    <tr>
      <td>field_id</td>
      <td>int</td>
      <td>The field id that the application was implemented</td>
    </tr>
    <tr>
      <td>type</td>
      <td>varchar(10)</td>
      <td>Defines the type of application and could be one of 'irrigation' or 'fertilization'</td>
    </tr>
    <tr>
      <td>suggested_amount</td>
      <td>json</td>
      <td>A json object with the keys type and amount. The key type take values 'water' or '19-6-15 (+7) +2MgO +0,5B'(fertilizer composition) in the case of irrigation and fertilization respectively. Similarly, the key amount is an integer and refers to the amount of water in qubic meters or the fertilizer amount in kg that is suggester to be applied to the field by the model. For example in the case of an irrigation advice {"type":"water","amount":300}
    </tr>
    <tr>
      <td>applied_amount</td>
      <td>json</td>
      <td>The amount of water or fertilizer that is actually applied on the field e.g. {"type":"water","amount":390}
    </tr>
    <tr>
      <td>applied_in</td>
      <td>float</td>
      <td>The timestamp that the application occurs</td>
    </tr>
    <tr>
      <td rowspan="6">advices_registry</td>
      <td>id</td>
      <td>int</td>
      <td>An advice unique identification number</td>
    </tr>
    <tr>
      <td>field_id</td>
      <td>int</td>
      <td>The field id that the advice was asked for</td>
    </tr>
    <tr>
      <td>type</td>
      <td>varchar(10)</td>
      <td>Defines the type of the advice and could be one of 'irrigation' or 'fertilization'</td>
    </tr>
    <tr>
      <td>status</td>
      <td>varchar(10)</td>
      <td>Defines the status of an irrigation advice. It can be one of 'ready', 'in_progress', 'cancelled', 'configuration_required'</td>
    </tr>
    <tr>
      <td>date_registered</td>
      <td>float</td>
      <td>The timestampt that the user asked for the advice</td>
    </tr>
    <tr>
      <td>date_created</td>
      <td>float</td>
      <td>The timestampt that the advice status switched to 'ready'</td>
    </tr>
    <tr>
      <td rowspan="3">measurement_translations</td>
      <td>measurement</td>
      <td>varchar(100)</td>
      <td>The name of the parameter that is measured. The nomenclature is mainly based on the <a href="https://cfconventions.org/Data/cf-standard-names/29/build/cf-standard-name-table.html">CF Standard Names<a></td>
    </tr>
    <tr>
      <td>el</td>
      <td>varchar(800)</td>
      <td> A name of a measured parameter expresed in a manner that the end user can understand in Greek language</td>
    </tr>
    <tr>
      <td>en</td>
      <td>varchar(800)</td>
      <td> A name of a measured parameter expresed in a manner that the end user can understand in English language</td>
    </tr>
  </tbody>
</table>

**Module Name: schemas**
<br>
**Version: 1.0.1**

Validates the data type before they are used by CRUD module methods creating classes inheriting from pydantic basemodel class.

**Module Name: crud**
<br>
**Version: 1.0.3**

Defines all the methods that Create, Read, Update and Delete
tables, rows, etc. from MySql database. It includes the
folloing classes-methods:
<br>
<br>
<table>
  <thead>
    <tr>
      <th>Class Name</th>
      <th>Method</th>
      <th>Short Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="4">User</td>
      <td>add</td>
      <td>Adds a new user<br><b>Arguments:</b><br><i>name(str)</i>: the cognito user id; <br><i>email(str)</i>: the user email; <br><i>subscription_expires_in(timestamp)</i>: users's expiration subscritpion timestamp</td>
    </tr>
    <tr>
      <td>get_by_name</td>
      <td>Returns an sqlalchemy object with the user id, name, email and subscription_expires_in info<br><b>Arguments</b><br><i>name(str)</i>: the cognito user id</td>
    </tr>
    <tr>
      <td>get_by_id</td>
      <td>Returns an sqlalchemy object with the user id, name, email and subscription_expires_in info<br><b>Arguments</b><br><i>user_id(int)</i>: the user id</td>
    </tr>
    <tr>
      <td>get_by_email</td>
      <td>Returns an sqlalchemy object with the user id, name, email and subscription_expires_in info<br><b>Arguments</b><br><i>email(str)</i>: the user email</td>
    </tr>
    <tr>
      <td rowspan="6">Stations</td>
      <td>add</td>
      <td>Adds a new station</td>
    </tr>
    <tr>
      <td>get_by_code</td>
      <td>By providing the station code it returns an sqlalchemy object with the station id, brand, model, code, date_created, longitude,
      latitude, elevation, access, name and icon_type</td>
    </tr>
    <tr>
      <td>get_by_brand</td>
      <td>By providing the station brand it returns an array of sqlalchemy objects equal to the stations of the provided brand. Each sqlalchemy onject provided infor for the station id, brand, model, code, date_created, longitude, latitude, elevation, access, name and icon_type</td>
    </tr>
    <tr>
      <td>get_by_access</td>
      <td>By providing a user id it returns an array of sqlalchemy objects with the stations that the use has an active subscription. Each sqlalchemy onject provided infor for the station id, brand, model, code, date_created, longitude, latitude, elevation, access, name and icon_type</td>
    </tr>
    <tr>
      <td>update_date_created</td>
      <td>By providing a station id and a timestamp it updates the date_created column value.</td>
    </tr>
    <tr>
      <td>delete_by_code</td>
      <td>It deletes a station entry for a provided station id.</td>
    </tr>
    <tr>
      <td rowspan="2">Gateways</td>
      <td>add</td>
      <td>Adds a new gateway</td>
    </tr>
    <tr>
      <td>get by code</td>
      <td>By providing the gateway code it returns an sqlalchemy object with the gateway id, brand, model, code, name and station_id</td>
    </tr>
    <tr>
      <td rowspan="3">RemoteTerminalUnits</td>
      <td>add</td>
      <td>Adds a new remote terminal unit</td>
    </tr>
    <tr>
      <td>get_by_code</td>
      <td>By providing a remote terminal unit code it returns an sqlalchemy object with the terminal unit id, brand, model, code, longitude, latitude, elevation, name and station_id</td>
    </tr>
    <tr>
      <td>get_by_station_id</td>
      <td>By providing a station id it returns an sqlalchemy object with the terminal unit id, brand, model, code, longitude, latitude, elevation, name and station_id</td>
    </tr>
    <tr>
      <td rowspan="3">SensorsMeters</td>
      <td>add</td>
      <td>Adds a new sensor or meter</td>
    </tr>
    <tr>
      <td>get_by_station_id</td>
      <td>By providing a station id it returns an sqlalchemy object with the sensor/meter id, type, measurement, unit, gauge_height, name, code,station_id and rtu_id</td>
    </tr>
    <tr>
      <td>get_by_rtu_id</td>
      <td>By providing a remote terminal unit id it returns an sqlalchemy object with the sensor/meter id, type, measurement, unit, gauge_height, name, code,station_id and rtu_id</td>
    </tr>
    <tr>
      <td>get_by_station_id_and_rtu_id</td>
      <td>By providing a station id and a remote terminal unit id it returns an sqlalchemy object with the sensor/meter id, type, measurement, unit, gauge_height, name, code,station_id and rtu_id</td>
    </tr>
    <tr>
      <td>get_by_id</td>
      <td>By providing a sensor/meter id it returns an sqlalchemy object with the sensor/meter id, type, measurement, unit, gauge_height, name, code,station_id and rtu_id</td>
    </tr>
    <tr>
      <td rowspan="2">MeasurementsTranslations</td>
      <td>add</td>
      <td>Adds a new measurement translation</td>
    </tr>
    <tr>
      <td>get_translation_by_measurement</td>
      <td>By providing a measurement it returns the corresponding description in all registered languages</td>
    </tr>
  </tbdody>
</table>

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
