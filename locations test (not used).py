## needs locations module by pythonista to function
import location
import time
from moving_average import GPS

gps_lat = GPS()
gps_long = GPS()
unfiltered = []
filtered = []
while not location.is_authorized()
    print ("Location services is not turned on.")
    time.sleep(1)

input("Enter to start.")
location.start_updates()
try:
    while True:
        coords = location.get_location()
        lat, long = coords['latitude'], coords['longitude']
        unfiltered.append([lat,long])
        filtered.append([gps_lat.add_avg(lat),gps_long.add_avg(long)])
        time.sleep(0.5)
except (KeyboardInterrupt, MemoryError):
    location.stop_updates()
    f = open('RawData.txt','w')
    f.write(unfiltered)
    f.close()
    f = open('FilteredData.txt','w')
    f.write(filtered)
    f.close()
