
# coding: utf-8

# In[51]:


from __future__ import print_function


# In[52]:


import json


# In[53]:


try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


# In[57]:


mode = "Json"
units = "metric"
apikey = sys.argv[1]
bus = sys.argv[2]


# In[58]:


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey,bus)
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[62]:
try: 
    busmta=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    numbus=len(busmta)

# In[63]:
except KeyError:
    busmta="Select Bus Service"
    numbus=0
    if numbus==0:
        print("Select Bus Service")




# In[ ]:


print("Bus Line : "+sys.argv[2])


# In[64]:


print("Number of Active Buses :"+str(numbus))


# In[66]:


for i in range(numbus):
    
    try:
        Long = busmta[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        Lat = busmta[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
    except KeyError:
        Long = "N/A"
        Lat = "N/A"

    print("Bus", str(i), "is at Latitude ", Lat, "and Longitude", Long)

