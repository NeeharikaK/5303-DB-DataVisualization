import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = "pk.eyJ1IjoibmVlaGFyaWthayIsImEiOiJjazJsOTlsYWcwNHFtM2JudHRpY2Y1ZnUzIn0.-9h08W2-BvmvhGfTO8Mobg"
mapbox_style = "mapbox://styles/neeharikak/ck3yt0g624vwr1clm0itq8t5r"
crash = db["plane_crashes"]
lats = []
lons = []
redlat300 = []
redlon300 = []
orangelat200 = []
orangelon200 = []
yellowlat100 = []
yellowlon100 = []
bluelat = []
bluelon = []

crashArray = [0, 0, 0 ,0]

for obj in crash.find():
    
    lats.append(obj["Latitude"])
    lons.append(obj["Longitude"])
    if obj["TotalFatalInjuries"] != '  ' and obj["TotalFatalInjuries"] is not None:
     if (int(obj["TotalFatalInjuries"]) > 300):
        redlat300.append(obj["Latitude"])
        redlon300.append(obj["Longitude"])
     elif (int(obj["TotalFatalInjuries"]) > 200):
        orangelat200.append(obj["Latitude"])
        orangelon200.append(obj["Longitude"])
     elif (int(obj["TotalFatalInjuries"]) > 100):
        yellowlat100.append(obj["Latitude"])
        yellowlon100.append(obj["Longitude"])
     else:
        bluelat.append(obj["Latitude"])
        bluelon.append(obj["Longitude"])



fig = go.Figure()

fig.add_trace(go.Scattermapbox(
                                    lat = redlat300,
                                    lon = redlon300,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "red"}
                                    )
                                )

fig.add_trace(go.Scattermapbox(
                                    lat = orangelat200,
                                    lon = orangelon200,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "orange"}
                                    )
                                )                                

fig.add_trace(go.Scattermapbox(
                                    lat = yellowlat100,
                                    lon = yellowlon100,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "yellow"}
                                    )
                                )

fig.add_trace(go.Scattermapbox(
                                    lat = bluelat,
                                    lon = bluelon,
                                    mode = "markers",   
                                    marker = {"size": 10, "color": "blue"}
                                    )
                                )      


fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=token,
            bearing=0,
            style=mapbox_style,
            center=go.layout.mapbox.Center(
                lat=33.930828,
                lon=-98.484879
            ),
            pitch=0,
            zoom=1
        ))

plotly.offline.plot(fig, filename='plane_crash.html')