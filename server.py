import time
from datetime import datetime

from flask import Flask, request, abort


app = Flask(__name__)

db = [
    {
        'name': 'Jack',
        'text': 'Hello',
        'time': time.time()
    },
    {
        'name': 'Mary',
        'text': 'Jack',
        'time': time.time()
    },
]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/status/')
def status():
    return json.dumps({
        'status': True,
        'name': 'Jack from ministry',
        'time': str(time.time())
        })

@app.route('/send', methods=['POST'])
def send():
    data = request.json
    #валидация данных
    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)
    
    name = data['name']
    text = data['text']
    if not 0 < len(name) <= 64:
        return abort(400)

    db.append(
        {
        'name': name,
        'text': text,
        'time': time.time()
    })

    return {}

@app.route('/messages')
def messages():

    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    filtered_messages = []
    
    for message in db:
        if message['time'] > after:
            filtered_messages.append(message)

    return {'messages': filtered_messages[:50]}


if __name__=='__main__':
    app.run(debug=True)
 