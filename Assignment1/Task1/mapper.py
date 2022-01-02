#!/usr/bin/env python3
import sys
import json
import math
from datetime import datetime   
#dict_op={}
for line in sys.stdin:
    line = json.loads(line) #json to python dict
    if math.isnan(line['Severity']) or math.isnan(line['Visibility(mi)']) or math.isnan(line['Precipitation(in)']):
        continue
    starttime = line['Start_Time']
    
    try:
        date=datetime.strptime(starttime ,'%Y-%m-%d %H:%M:%S')
    except:  #if format doesn't match ie microseconds
        starttime=starttime.split(".")[0]
        date=datetime.strptime(starttime ,'%Y-%m-%d %H:%M:%S')

    hour=date.hour
    
    severity = line['Severity']
    sunrisesunset = line['Sunrise_Sunset']
    visibility = line['Visibility(mi)']
    precipitation = line['Precipitation(in)']
    weathercondition = line['Weather_Condition']
    description = line['Description']
    
    
    if description.lower().find("lane blocked")!=-1 or description.lower().find("shoulder blocked")!=-1 or description.lower().find("overturned vehicle")!=-1:
        if severity >= 2 and visibility <= 10 and precipitation >= 0.2:
            if sunrisesunset == "Night":
                if weathercondition in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]:
                    #dict_op[hour]=dict_op.setdefault(hour,0)+1
                    #print '%d\t%s' % (hour,1)
                    print(f"{hour}")
#dict_op = {key:dict_op[key] for key in sorted(dict_op)}  reducer file code
#print(dict_op)                 

                        


        
