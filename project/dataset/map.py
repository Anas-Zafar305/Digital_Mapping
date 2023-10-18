import folium
import pandas as pd
import os
import json

states = os.path.join('../project/dataset/' , 'us-states.json')
data = os.path.join('../project/dataset/' , 'data.csv')
state_data = pd.read_csv(data)
print(state_data)