import matplotlib.pyplot as plt
# Open File
f = open("tempdata.txt", "r")
Data Analysis Example
# Transform File Data into x Array and y Array that can be used for plotting x = []
y = []
k=0
for record in f:
    record = record.replace("\n", "")
    record = record.split(";")
    x.append(int(record[0]))
    y.append(int(record[1]))
    k=k+1
f.close()

plt.plot(x,y, '-o')
plt.title('Temperature Data from TC74 Sensor')
plt.xlabel('Time[s]')
plt.ylabel('Temperature[°C]')
plt.grid()
plt.show()

