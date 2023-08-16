from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_socketio import SocketIO
from app.config import Config

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = Config.key
socketio = SocketIO(app)
#TBAR = DebugToolbarExtension(app)

from app import routes  # Import sau khi đã tạo app và socketio

