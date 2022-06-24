#Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs

#Enter the directory of the csv file here 
data = pd.read_csv("")

#Defining the results from the csv files in arrays
lats = data.iloc[:,11].values
lons = data.iloc[:,12].values

# Set up a standard map for lat,lon data.
ax=plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()
ax.coastlines()


# Plotting the longitude and latitude 
plt.plot([lons], [lats],
         color='red', linewidth=2, marker='o',
         transform=ccrs.Geodetic()
         )
plt.title("Experiment's Path")

plt.show()
