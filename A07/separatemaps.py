"""
Plots each collection on a separate map.
"""

import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo
from geo import mapbox_access_token

# I make collections a list because my program will loop through each one,
# opening each map in a new browser tab.
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
collections = [db["airports"], db["earthquakes"], 
    db["volcanos"], db["ufos"]]

# Filename and marker color need to change with the collection being mapped
names = ["airports", "earthquakes", "volcanos", "ufos"]
color = ["green", "orange", "red", "blue"]
index = 0

# I will provide my token on request.
#token = token = open(r"mapbox_token.txt").read()

mapbox_style = "mapbox://styles/neeharikak/ck3yt0g624vwr1clm0itq8t5r"


lat = []
lon = []

for collection in collections:
    for obj in collection.find():
        lat.append(obj["latitude"])
        lon.append(obj["longitude"])

    fig = go.Figure(go.Scattermapbox(
        lat = lat,
        lon = lon,
        mode = 'markers',
        marker=go.scattermapbox.Marker(size=9, color = color[index])
       ))



    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            style=mapbox_style,
            center=go.layout.mapbox.Center(
                lat=33.930828,
                lon=-98.484879
            ),
            pitch=0,
            zoom=3
        ))

    plotly.offline.plot(fig, filename= names[index] +".html")
    index += 1
    lat.clear()
    lon.clear()
