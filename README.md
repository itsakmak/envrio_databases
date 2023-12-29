# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and Influx databases.

## Modules:

**Module Name: engine**
<br>
**Version: 1.0.8**

Creates the engine that connects an app to the MySql database.

**Module Name: models**
<br>
**Version: 1.0.6**

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
      <td>User's subscription expiration timestamp</td>
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
       <td>latest_update</td>
       <td>float</td>
       <td>The timestamp of the station last data update</td>
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
      <td rowspan="9">monitored_parameters</td>
      <td>id</td>
      <td>int</td>
      <td>Parameter unique identification number</td>
    </tr>
    <tr>
      <td>device_type</td>
      <td>varchar(7)</td>
      <td>Depending on the type of device that monitores the parameter. It's 'sensor', 'meter', or 'calc' if the parameter is monitored by a sensor, a meter or is a formula result, respectively</td>
    </tr>
    <tr>
      <td>measurement</td>
      <td>varchar(100)</td>
      <td>The name of the parameter that is measured. The nomenclature is mainly based on the <a href="https://cfconventions.org/Data/cf-standard-names/29/build/cf-standard-name-table.html">CF Standard Names<a></td>
    </tr>
    <tr>
      <td>unit</td>
      <td>varchar(20)</td>
      <td>The unit that the parameter is reported</td>
    </tr>
    <tr>
      <td>device_height</td>
      <td>float</td>
      <td>The distance of the device, that monitors the parameter, from a reference surface (land or sea) in meters. If the device is above the reference surface the device height takes positive values, while in the case of installations within soil or below the sea surface negative</td>
    </tr>
    <tr>
      <td>name</td>
      <td>varchar(100)</td>
      <td>Paremeter name as defined by the user</td>
    </tr>
    <tr>
      <td>code</td>
      <td>varchar(100)</td>
      <td>Parameter id in the data provider API</td>
    </tr>
    <tr>
      <td>station_id</td>
      <td>int</td>
      <td>The id of the station that the parameter is measured by</td>
    </tr>
    <tr>
      <td>rtu_id</td>
      <td>int</td>
      <td>The id of the remote terminal unit that the parameter is measured by. Default value is None</td>
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
      <td>id</td>
      <td>int</td>
      <td>A field unique identification number</td>
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
**Version: 1.0.2**

Validates the data type before they are used by CRUD module methods creating classes inheriting from pydantic basemodel class.

**Module Name: crud**
<br>
**Version: 1.0.10**

Defines all the methods that Create, Read, Update and Delete
tables, table rows, etc. from MySql database. It includes the
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
      <td>Adds a new user to MySql database<br><b>Arguments:</b><br><span class=highlight><i>name(str)</i></span>: the cognito user id; <br><span class=highlight><i>email(str)</i></span>: the user email; <br><span class=highlight><i>subscription_expires_in(timestamp)</i></span>: user's subscription expiration timestamp</td>
    </tr>
    <tr>
      <td>get_by_name</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>user id</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>email</i></span> and <span class=highlight><i>subscription_expires_in info</i></span><br><b>Arguments</b><br><span class=highlight><i>name(str)</i><span>: the cognito user id</td>
    </tr>
    <tr>
      <td>get_by_id</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>user id</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>email</i></span> and <span class=highlight><i>subscription_expires_in info</i></span><br><b>Arguments</b><br><span class=highlight><i>user_id(int)</i></span>: the user id</td>
    </tr>
    <tr>
      <td>get_by_email</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>user id</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>email</i></span> and <span class=highlight><i>subscription_expires_in info</i></span><br><b>Arguments</b><br><span class=highlight><i>email(str)</i></span>: the user email</td>
    </tr>
    <tr>
      <td rowspan="7">Stations</td>
      <td>add</td>
      <td>Adds a new station to MySql database<br><b>Arguments</b><br><span class=highlight><i>brand(str)</i></span>: station's brand<br><span class=highlight><i>model(str)</i></span>: station's specific model<br><span class=highlight><i>code(str)</i></span>: station's code in provider's API<br><span class=highlight><i>date_created(int)</i></span>: station's installation timestamp<br><span class=highlight><i>longitude(decimal)</i></span>: station's longitude<br><span class=highlight><i>latitude(decimal)</i></span>: station's latitude<br><span class=highlight><i>elevation(int)</i></span>: station's elevation<br><span class=highlight><i>access(int)</i></span>: the user ids that have an active subscription<br><span class=highlight><i>name(json)</i></span>: A dictionary with station's name in different languages<br><span class=highlight><i>icon_type(str)</i></span>: one of 'hydro', 'meteo', 'coastal' depending on station's type</td>
    </tr>
    <tr>
      <td>get_by_code</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>station id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>date_created</i></span>, <span class=highlight><i>latest_update</i></span>, <span class=highlight><i>longitude</i></span>, <span class=highlight><i>latitude</i></span>, <span class=highlight><i>elevation</i></span>, <span class=highlight><i>access</i></span>, <span class=highlight><i>name</i></span> <span class=highlight><i>and icon_type</i></span><br><b>Arguments</b><br><span class=highlight><i>code(str)</i></span>: the station's id in provider's API</td>
    </tr>
    <tr>
      <td>get_by_brand</td>
      <td>Returns a list of named tuples. The list length is equal to the stations of the given brand. Each named tuple has the name fields <span class=highlight><i>station id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>date_created</i></span>, <span class=highlight><i>latest_update</i></span>, <span class=highlight><i>longitude</i></span>, <span class=highlight><i>latitude</i></span>, <span class=highlight><i>elevation</i></span>, <span class=highlight><i>access</i></span>, <span class=highlight><i>name</i></span> <span class=highlight><i>and icon_type</i></span><br><b>Arguments</b><br><span class=highlight><i>brand(str)</i></span>: a station brand</td>
    </tr>
    <tr>
      <td>get_by_access</td>
      <td>Returns a list of named tuples. The list length is equal to the stations that a user has an active subscription for. Each named tuple has the name fields <span class=highlight><i>station id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>date_created</i></span>, <span class=highlight><i>latest_update</i></span>, <span class=highlight><i>longitude</i></span>, <span class=highlight><i>latitude</i></span>, <span class=highlight><i>elevation</i></span>, <span class=highlight><i>access</i></span>, <span class=highlight><i>name</i></span> <span class=highlight><i>and icon_type</i></span><br><b>Arguments</b><br><span class=highlight><i>user_id(int)</i></span>: the user id</td>
    </tr>
    <tr>
      <td>update_date_created</td>
      <td>Updates the date_created column value<br><b>Arguments</b><br><i>station_id(int)</i>: a station id<br><i>new_datetime(ing)</i>: the new date time timestamp</td>
    </tr>
    <tr>
      <td>update_latest_update</td>
      <td>The date-time of the last data update<br><b>Arguments</b><br><span class=highlight><i>station_id(int)</i></span>: a station id<br><span class=highlight><i>new_datetime(int)</i></span>: the new date time timestamp</td>
    </tr>
    <tr>
      <td>delete_by_code</td>
      <td>It deletes a station entry for a provided station id<br><b>Arguments</b><br><span class=highlight><i>code(str)</i></span>: the station's id as defined in provider's API</i>: </td>
    </tr>
    <tr>
      <td rowspan="2">Gateways</td>
      <td>add</td>
      <td>Adds a new gateway<br><b>Arguments</b><br><span class=highlight><i>brand(str)</i></span>: gateway's brand<br><span class=highlight><i>model(str)</i></span>: gateway's specific model<br><span class=highlight><i>code(str)</i></span>: gateway's id in provider's API<br><span class=highlight><i>name(str)</i></span>: gateway's user defined name<br><span class=highlight><i>station_id(int)</i></span>: the station id that gateway is connected to</td>
    </tr>
    <tr>
      <td>get by code</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>gateway id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>name</i></span> and <span class=highlight><i>station_id</i></span><br><b>Arguments</b><br><span class=highlight><i>code(str)</i></span>: gateways's id is provider's API</td>
    </tr>
    <tr>
      <td rowspan="3">RemoteTerminalUnits</td>
      <td>add</td>
      <td>Adds a new remote terminal unit in MySql database<br><b>Arguments</b><br><span class=highlight><i>brand(str)</i></span>: remote terminal unit's brand<br><span class=highlight><i>model(str)</i></span>: remote terminal unit's specific model<br><span class=highlight><i>code(str)</i></span>: remote terminal unit's id in provider's API<br><span class=highlight><i>longitude(decimal)</i></span>: remote terminal unit's longitude<br><span class=highlight><i>latitude(decimal)</i></span>:  remote terminal's unit longitude<br><span class=highlight><i>evelation(int)</i></span>: remote terminal unit's elevation<br><span class=highlight><i>name(json)</i></span>: a dictionaly with a name assigned by the user to the remote terminal uni in different languages<br><span class=highlight><i>station_id(int)</i></span>: the station id that the remote terminal unit is paired with</td>
    </tr>
    <tr>
      <td>get_by_code</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>longitude</i></span>, <span class=highlight><i>latitude</i></span>, <span class=highlight><i>elevation</i></span>, <span class=highlight><i>name</i></span> and <span class=highlight><i>station_id</i></span><br><b>Arguments</b><br><span class=highlight><i>code(str)</i></span>: the remote terminal unit's code in providers API</td>
    </tr>
    <tr>
      <td>get_by_station_id</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>brand</i></span>, <span class=highlight><i>model</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>longitude</i></span>, <span class=highlight><i>latitude</i></span>, <span class=highlight><i>elevation</i></span>, <span class=highlight><i>name</i></span> and <span class=highlight><i>station_id</i></span><br><b>Arguments</b><br><span class=highlight><i>station_id(int)</i></span>: the station id that remote terminal unit is paired with</td>
    </tr>
    <tr>
      <td rowspan="5">MonitoredParameters</td>
      <td>add</td>
      <td>Adds a new sensor or meter to MySql database<br><b>Arguments</b><br><span class=highlight><i>device_type(str)</i></span>: can be one of <span class=highlight2><i>sensor</i></span>, <span class=highlight2><i>meter</i></span> or <span class=highlight2><i>calc</i></span><br><span class=highlight><i>measurement(str)</i></span>: monitored parameter's name<br><span class=highlight><i>unit(str)</i></span>: monitored parameter's unit<br><span class=highlight><i>device_height(float)</i></span>: the device distance below (negative) or above (positive) the reference surface (soil or sea) in meters<br><span class=highlight><i>name(str)</i></span>: a name assigned by the user to the parameter<br><span class=highlight><i>code(str)</i></span>: the parameter id in provider's API<br><span class=highlight><i>station_id(int)</i></span>: the station id that the parameter is monitored by<br><span class=highlight><i>rtu_id</i></span>: the remote terminal unit id that the parameter is monitored by. Default value is None</td>
    </tr>
    <tr>
      <td>get_by_station_id</td>
      <td>Returns a list of named tuples with the parameters that are monitored by the given station id. Each named tuple object includes the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>device_type</i></span>, <span class=highlight><i>measurement</i></span>, <span class=highlight><i>unit</i></span>, <span class=highlight><i>device_height</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>station_id</i></span> and <span class=highlight><i>rtu_id</i></span><br><b>Arguments</b><br><span class=highlight><i>station_id(int)</i></span>: the station id that the parameter is monitored by</td>
    </tr>
    <tr>
      <td>get_by_rtu_id</td>
      <td>Returns a list of named tuples with the parameters that are monitored by the given rtu id. Each named tuple object includes the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>device_type</i></span>, <span class=highlight><i>measurement</i></span>, <span class=highlight><i>unit</i></span>, <span class=highlight><i>device_height</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>station_id</i></span> and <span class=highlight><i>rtu_id</i></span><br><b>Arguments<br></b><span class=highlight><i>rtu_id(int)</i></span>: the remote terminal unit id that the parameter is monitored by</td>
    </tr>
    <tr>
      <td>get_by_station_id_and_rtu_id</td>
      <td>Returns a list of named tuples with the parameters that are monitored by the given station & rtu ids. Each named tuple object includes the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>device_type</i></span>, <span class=highlight><i>measurement</i></span>, <span class=highlight><i>unit</i></span>, <span class=highlight><i>device_height</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>station_id</i></span> and <span class=highlight><i>rtu_id</i></span><br><b>Arguments</b><br><span class=highlight><i>station_id(int)</i></span>: the station id that the parameter is monitored by<br><span class=highlight><i>rtu_id(int)</i></span>: the remote terminal unit id that the parameter is monitored by</td>
    </tr>
    <tr>
      <td>get_by_id</td>
      <td>Returns a named tuple object with the named fields <span class=highlight><i>id</i></span>, <span class=highlight><i>device_type</i></span>, <span class=highlight><i>measurement</i></span>, <span class=highlight><i>unit</i></span>, <span class=highlight><i>device_height</i></span>, <span class=highlight><i>name</i></span>, <span class=highlight><i>code</i></span>, <span class=highlight><i>station_id</i></span> and <span class=highlight><i>rtu_id</i></span><br><b>Arguments</b><br><span class=highlight><i>id(int)</i></span>: parameter id</td>
    </tr>
  </tbdody>
</table>
<br>

**Module Name: influx**
<br>
**version: 1.0.2**

Connects to the InfluxDB database and defines all the required 
methods for data management and bucket configuration:
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
      <td rowspan=1>InfluxConnector</td>
      <td>__init__</td>
      <td>Initializes an influx instance<br><b>Arguments</b><br><span class=highlight><i>bucket_name(str)</i></span>: the desired influx bucket<br><span class=highlight><i>organization(str)</i></span>: the organization that owns influx<br><span class=highlight><i>conf_file</i></span>: the name of the file that contains influx credentials</td>
    </tr>
    <tr>
      <td rowspan=3>DataManagement</td>
      <td>write_point</td>
      <td>Inserts data points to the database<br><b>Arguments</b><br><span class=highlight><i>measurement(str)</i></span>: The name of the parameter that is measured<br><span class=highlight><i>sensor_id(int)</i></span>: the sensor id in MySql MeasuredParameters table<br><span class=highlight><i>unit(str)</i></span>: the unit that the parameter is expressed<br><span class=highlight><i>data(dict)</i></span>: a dictionary with keys <span class=highlight2><i>date_time</i></span> and <span class=highlight2><i>values</i></span> that contains the measured data and their timestamps</td>
    </tr>
    <tr>
      <td>delete_rows</td>
      <td>Deletes data points from the database for a given time range<br><b>Arguments</b><br><span class=highlight><i>measurement(str)</i></span>: The name of the parameter from which data will be deleted<br><span class=highlight><i>start(str)</i></span>: A date-time in <i>ISO 8601</i> format. The beginning of the time period that data points will be deleted<br><span class=highlight><i>stop(str)</i></span>: A date-time in <i>ISO 8601</i> format. The end of the time period that data points will be deleted<br><span class=highlight><i>tag(str)</i></span>: A measured parameter id as defined in MySql MeasuredParemeters table</td>
    </tr>
    <tr>
      <td>query_data</td>
      <td>Returns a dataframe with the queried data<br><b>Arguments</b><br><span class=highlight><i>measurement(str)</i></span>: The name of the parameter that data should be retrieved<br><span class=highlight><i>sensor_id(int)</i></span>: a parameter id from MySql MeasuredParemeters table<br><span class=highlight><i>unit(srt)</i></span>: the unit that the parameter is expressed<br><span class=highlight><i>start(str)</i></span>: A date-time in <i>ISO 8601</i> format. The beginning of the time period that data points will be retrieved<br><span class=highlight><i>stop(str)</i></span>: A date-time in <i>ISO 8601</i> format. The end of the time period that data points will be retrieved<br></td>
    </tr>
    <tr>
      <td rowspan=2>BucketConfiguration</td>
      <td>list_buckets</td>
      <td>Returns a list with the existing Bucket class objects</td>
    </tr>
    <tr>
      <td>update_bucket</td>
      <td>Updates a Bucket retention rules<br><b>Arguments</b><br><span class=highlight><i>type(str)</i></span>: a string that represents Bucket type e.g., <br><p style="background-color: lightblue;"><i>expire</i></p><br><span class=highlight><i>data_duration(int)</i></span>: the data duration in seconds. Default is 0, corresponding to <span class=highlight2><i>infinite</i></span><br><span class=highlight><i>shard_group_duration(int)</i></span>: the shard group duration in seconds. Default value is set to 630,720,000 secs (roughly 20 years)<br><span class=highlight><i>description(str)</i></span>: a short descrption related with the update purpose<br></td>
    </tr>
  </tbdody>
</table>


<style>
  .highlight {
    background-color: #888; /* Set the background color */
    padding: 5px; /* Add some padding for better visibility */
  }
  .highlight2{
    background-color: #999; /* Set the background color */
    padding: 5px; /* Add some padding for better visibility */
    color: red;    
  }
</style>
