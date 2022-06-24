#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Enter the directory of the csv file here 
data = pd.read_csv("")

#Variable containing the readings
elev = data.iloc[:,13].values


#Changing the graph title and the axis
plt.title("Elevation")
plt.xlabel("time")
plt.ylabel("Elevation/m")


#To Remove the date and give the time only
x = data.iloc[:,0] 
time = []
for i in x:
    time.append(i.split()[1][:8])

#Plotting the Elevation
plt.plot(elev)

#Making a variable to use as the x axis with certain time periods from the CSV file
labels = [time[0], time[200], time[400], time[600], time[800], time[1000], time[1200], time[1400], time[1600], time[1968]]

plt.xticks(np.arange(0, 1969, 200), labels)

plt.legend()
plt.show()
