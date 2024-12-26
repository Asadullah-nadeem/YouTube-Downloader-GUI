import socketio
from flask import Flask

# Initialize Flask and SocketIO
app = Flask(__name__)
sio = socketio.Server()

# Attach the SocketIO server to the Flask app
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
