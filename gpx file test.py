from weighted_moving_average import GPS
#import matplotlib.pyplot as plt
n = 15
raw_data_lat = []
raw_data_long = []
avg_data_lat = []
avg_data_long = []

gps_lat = GPS(n)
gps_long = GPS(n)

f = open('source_data.txt', 'r')
for line in f:
    if line[0] != "T":
        continue
    data = line.split()
    raw_data_lat.append(float(data[3]))
    raw_data_long.append(float(data[4]))
    avg_data_lat.append(gps_lat.add_avg(float(data[3])))
    avg_data_long.append(gps_long.add_avg(float(data[4])))

f.close()

f = open('weighted_raw_data.txt', 'w')
for i in range(len(raw_data_lat)):
    f.write('['+str(raw_data_lat[i])+', '+str(raw_data_long[i])+'],\n')
f.close()

f = open('weighted_avg_data.txt', 'w')
for i in range(len(avg_data_lat)):
    f.write('['+str(avg_data_lat[i])+', '+str(avg_data_long[i])+'],\n')
f.close()

##raw_line = plt.plot(raw_data_lat,raw_data_long)
##avg_line = plt.plot(avg_data_lat,avg_data_long)
##plt.show()
