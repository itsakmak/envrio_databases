__version__='1.0.1'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-16'

from influxdb_client import InfluxDBClient, Bucket, BucketRetentionRules
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
from datetime import datetime, timedelta

class InfluxDB(object):

    def __init__(self,bucket_name,organization,conf_file):
        self.client = InfluxDBClient.from_config_file(conf_file)
        self.bucket_name = bucket_name
        self.org = organization

    def write_point(self,measurement,sensor_id,unit,data):
        write_api = self.client.write_api(write_options=SYNCHRONOUS)
        if self.client.ping():
            records =[]
            for i in range(0,len(data['date_time'])):
                point = {
                    'measurement': measurement,
                    'tags': {'sensor_id': sensor_id},
                    'fields': {unit: float(data['values'][i]) if data['values'][i] is not None else data['values'][i]},
                    'time': data['date_time'][i].strftime('%Y-%m-%dT%H:%M:%S')
                    }
                records.append(point)
            print(f'\nBucket: {self.bucket_name}')
            print(f'\nMeasurement: {measurement}')
            print(f'\nRecords: {records}')
            write_api.write(bucket = self.bucket_name, org = self.org,record = records)            

    def delete_rows(self,measurement,start = pd.to_datetime("1970-01-01"),stop = pd.to_datetime(datetime.now()),tag = None):
        if self.client.ping():
            # Define api methods
            delete_api = self.client.delete_api()
            # Delete Points
            delete_api.delete(start,stop,predicate = f'_measurement = "{measurement}" and sensor_id = "{tag}"',bucket = self.bucket_name,org = self.org)
        else:
            raise Exception("Connection to InfluxDB failed")

    def query_data(self,measurement,sensor_id,unit,start = (datetime.now() - timedelta(days = 3)),stop = datetime.now()):
        if self.client.ping():
            query_api = self.client.query_api()
            data_frame = query_api.query_data_frame(f'''from(bucket:"{self.bucket_name}") 
                                                        |> range(start: {start.strftime("%Y-%m-%dT%H:%M:%SZ")}, stop: {stop.strftime("%Y-%m-%dT%H:%M:%SZ")}) 
                                                        |> filter(fn: (r) => r["_measurement"] == "{measurement}" and r["sensor_id"] == "{str(sensor_id)}")
                                                        |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
                                                        |> keep(columns: ["_time","sensor_id", "{unit}"])''')
            return data_frame
        else:
            raise Exception("Connection to InfluxDB failed")
        
    def list_buckets(self):
        if self.client.ping():
            buckets_api = self.client.buckets_api()
            buckets = buckets_api.find_buckets().buckets
            return print("\n".join([f" ---\n ID: {bucket.id}\n Name: {bucket.name}\n Retention: {bucket.retention_rules}"
                                for bucket in buckets]))
        else:
            raise Exception("Connection to InfluxDB failed")
        
    def update_bucket(self,type='expire',data_duration=0,shard_group_duration=630720000,description='Update to a 20 years shard group duration'):
        buckets_api=self.client.buckets_api()
        bucket_info=buckets_api.find_bucket_by_name(self.bucket_name)
        bucket_id="\n".join([f"{bucket_info.id}"])
        org_id ="\n".join([f"{bucket_info.org_id}"])
        bucket_update = Bucket(
                                description = description,
                                id = bucket_id,
                                name = self.bucket_name,
                                org_id = org_id,
                                retention_rules = [BucketRetentionRules(every_seconds = data_duration,
                                                                        shard_group_duration_seconds = shard_group_duration,
                                                                        type = type)])
        buckets_api.update_bucket(bucket = bucket_update)
        return print(buckets_api.find_bucket_by_name(self.bucket_name))

