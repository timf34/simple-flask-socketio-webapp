import logging
import eventlet
from flask import Flask, render_template
from flask_socketio import SocketIO

socketio = SocketIO(logger=True, engineio_logger=True, async_mode='eventlet', cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'
    app.logger.setLevel(logging.INFO)

    socketio.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('message')
    def handle_message(message):
        app.logger.info('Received message: %s', message)
        socketio.emit('message', message)

    def background_task_example():
        """Example of how to use start_background_task."""
        while True:
            socketio.sleep(10)
            app.logger.info("Background task!")
            socketio.emit('message', 'This is a message from the background task.')

    socketio.start_background_task(background_task_example)
    return app

application = create_app()

if __name__ == '__main__':
    socketio.run(application)
