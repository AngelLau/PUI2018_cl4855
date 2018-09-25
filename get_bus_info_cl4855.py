from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

mode = "Json"
units = "metric"
apikey = sys.argv[1]
bus = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus)
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busmta=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

numbus=len(busmta)

fout = open(sys.argv[3], "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

for i in range(numbus):
    Lat = busmta[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Long = busmta[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    
    try:
        StopName = busmta[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        StopStatus =busmta[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    
    except KeyError:
        StopName = "N/A"
        StopStatus = "N/A"
    fout.write(("%s,%s,%s,%s\n")%(Lat,Long,StopName,StopStatus))