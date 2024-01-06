# Envrio Databases Library

This repository contains the library that manages the Envrio MySql and Influx databases.

It consists of the following modules

## Modules:

**Module Name: engine**
<br>
**Version: 1.0.8**

**Module Name: models**
<br>
**Version: 1.0.6**

**Module Name: schemas**
<br>
**Version: 1.0.2**

**Module Name: crud**
<br>
**Version: 1.0.10**

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
      <td>Updates a Bucket retention rules<br><b>Arguments</b><br><span class=highlight><i>type(str)</i></span>: a string that represents Bucket type e.g., <br><span class=highlight><i>expire</i></span><br><span class=highlight><i>data_duration(int)</i></span>: the data duration in seconds. Default is 0, corresponding to <span class=highlight2><i>infinite</i></span><br><span class=highlight><i>shard_group_duration(int)</i></span>: the shard group duration in seconds. Default value is set to 630,720,000 secs (roughly 20 years)<br><span class=highlight><i>description(str)</i></span>: a short descrption related with the update purpose<br></td>
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
