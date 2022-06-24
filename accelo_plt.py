#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Enter the directory of the CSV file here  
data = pd.read_csv("")

#Variables containing the x,y,z readings of the sensor
acc_x = data.iloc[:,4].values
acc_y = data.iloc[:,5].values
acc_z = data.iloc[:,6].values


#Changing the graph title and the axis
plt.title("Absolute Acceleration")
plt.xlabel("time")
plt.ylabel("Acceleration/g")


#To Remove the date and give the time only
x = data.iloc[:,0] 
time = []
for i in x:
    time.append(i.split()[1][:8])

#Getting the absolute readings and storing them in a variable
resultant_value = np.linalg.norm([acc_x,acc_y,acc_z],axis=0)

#Plotting the Absolute Acceleration
plt.plot(resultant_value,label="Absolute Acceleration")

#Making a variable to use as the x axis with certain time periods from the CSV file
labels = [time[0], time[200], time[400], time[600], time[800], time[1000], time[1200], time[1400], time[1600], time[1968]]

plt.xticks(np.arange(0, 1969, 200), labels)

plt.legend()
plt.show()


