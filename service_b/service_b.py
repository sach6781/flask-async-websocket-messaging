import asyncio
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('message_from_b')
def handle_message(message):
    print('Received message from Service A:', message)
    asyncio.run(send_message_to_a(message))


async def send_message_to_a(message):
    await asyncio.sleep(1)  # Simulate some async work
    socketio.emit('message_from_a', message)


if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True)
