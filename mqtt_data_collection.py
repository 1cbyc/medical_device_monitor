import paho.mqtt.client as mqtt
import pandas as pd
import json

data = []

def on_message(client, userdata, message):
    global data
    payload = json.loads(message.payload.decode())
    data.append(payload)
    df = pd.DataFrame(data)
    df.to_csv('data/real_time_data.csv', index=False)

client = mqtt.Client()
client.on_message = on_message
client.connect('mqtt.broker.url', 1883, 60)
client.subscribe('medical/devices')
client.loop_forever()
