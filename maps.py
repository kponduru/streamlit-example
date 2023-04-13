import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# create a map object with India's coordinates
map = Basemap(llcrnrlon=68,llcrnrlat=7,urcrnrlon=89,urcrnrlat=35, resolution='l')

# draw coastlines and country boundaries
map.drawcoastlines()
map.drawcountries()

# fill the land with a light green color
map.fillcontinents(color='lightgreen',lake_color='white')

# draw the meridians and parallels
map.drawmeridians(range(60,100,5),labels=[False,False,False,True])
map.drawparallels(range(0,40,5),labels=[True,False,False,False])

# add a title
plt.title('Map of India')

# show the map
plt.show()
