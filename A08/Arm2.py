
import numpy as np 
import pandas as pd
import plotly
import plotly.graph_objects as go
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["armageddon"]
token = "pk.eyJ1IjoibmVlaGFyaWthayIsImEiOiJjazJsOTlsYWcwNHFtM2JudHRpY2Y1ZnUzIn0.-9h08W2-BvmvhGfTO8Mobg"
volc = db["volcanos"]
mapbox_style = "mapbox://styles/neeharikak/ck3yt0g624vwr1clm0itq8t5r"

listvolcanos = []
lats = []
lons = []
for obj in volc.find():
    listvolcanos.append(db["volcanos"].find().sort([("PEI", -1)]))
    lats.append(obj["latitude"])
    lons.append(obj["longitude"])
fig = go.Figure()

fig.add_trace(go.Scattermapbox(
                                    lat = lats,
                                    lon = lons,
                                    mode = "markers",   
                                    marker = {"size":[30, 20, 10],
                                    "color":["Red", "Orange", "Yellow"]}
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
            zoom=3
        ))

fig.show()
plotly.offline.plot(fig, filename='listvolcanos.html')

