import time
from datetime import datetime
import requests


after = 0

def print_message(message):
    dt = datetime.fromtimestamp(message['time'])
    print(dt.strftime('%H:%M:%S'), message['name'])
    print(message['text'])
    print()

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages', 
        params={'after': after}
    )
    
    messages = response.json()['messages']

    if messages:
        for message in messages:
            print_message(message)

        after = messages[-1]['time']

    time.sleep(1)