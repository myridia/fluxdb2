#!/usr/bin/env python3

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

#replace later with your name
bucket="rate" 

# replace later with your token
token = "Rym025SJu7c10FVdf05TBbg5XIf6s0NdSY05f8C4sjqCD8VBmsvsjTEaNbE6rLB8MqCdxldyFRsF4ePYGi-ZzA=="

#replace later with your orgname
org = "test"

url = "http://127.0.0.1:8086"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
query_api = client.query_api()

query = 'from(bucket:"rate")\
|> range(start: -100m)\
|> filter(fn:(r) => r._measurement == "EXO")\
|> filter(fn:(r) => r.name == "Exo")\
|> filter(fn:(r) => r._field == "rate")'

result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)
