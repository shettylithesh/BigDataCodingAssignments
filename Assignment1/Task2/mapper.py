#!/usr/bin/env python3

import sys
import json
import requests
import math
from datetime import datetime

latitude1 = float(sys.argv[1])
longitude1 = float(sys.argv[2])
coord1 = [latitude1, longitude1]
d = sys.argv[3]
url = "http://20.185.44.219:5000/"

for line in sys.stdin:
    line = json.loads(line)
    if math.isnan(line['Start_Lat']) or math.isnan(line['Start_Lng']):
        continue
    latitude2 = float(line['Start_Lat']) 
    longitude2 = float(line['Start_Lng']) 
    coord2 = [latitude2, longitude2]
    distance = math.dist(coord1, coord2)

    params = {"latitude":latitude2, "longitude":longitude2}
    if distance < float(d):
        r = requests.post(url, json = params)
        r = json.loads(r.text)
        city = r['city']
        state = r['state']
        if city != None and  state!=None:
        	print(state+","+city+",1")
