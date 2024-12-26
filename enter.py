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
write_api = client.write_api(write_options=SYNCHRONOUS)
   
for i in range(30):
  point = (
    Point("EXO")
    .tag("name", "Exo")
    .field("rate", "v-{0}".format(i))
  )
  print("...write data 30/{0}".format(i))

  
  write_api.write(bucket=bucket, org="test", record=point)
  time.sleep(2) # separate points by 1 second
  
