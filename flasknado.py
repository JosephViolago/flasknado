"""Flasknado! - A simple example of using Flask and Tornado
together.

"""

from __future__ import print_function
from flask import Flask, render_template
from tornado.wsgi import WSGIContainer
from tornado.web import Application, FallbackHandler, StaticFileHandler
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
import sys

class WebSocket(WebSocketHandler):
    def open(self):
        print("Socket opened.")

    def on_message(self, message):
        self.write_message("Received: " + message)
        print("Received message: " + message)

    def on_close(self):
        print("Socket closed.")

app = Flask('flasknado')

@app.route('/')
def index():
    return render_template('index.html')

def startTornado():
    server.listen(8080)
    IOLoop.instance().start()

def stopTornado():
    print("\nKeyboardInterrupt; Tornado is shutting down now.")
    IOLoop.instance().stop()
    sys.exit(0)

if __name__ == "__main__":
    container = WSGIContainer(app)
    server = Application([
        (r'/(favicon.ico)', StaticFileHandler, {'path': 'static'}),
        (r'/websocket/', WebSocket),
        (r'.*', FallbackHandler, dict(fallback=container))
    ])

    try:
        startTornado()
    except (KeyboardInterrupt, SystemExit):
        stopTornado()
