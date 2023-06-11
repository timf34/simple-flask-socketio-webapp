import logging
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.logger.setLevel(logging.INFO)
# TODO: note there's no CORS here; implement this and test in a bit.
socketio = SocketIO(app, logger=True, engineio_logger=True)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    app.logger.info('Received message: %s', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app)
