from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import rethinkdb as r

r.connect('35.166.62.31',28015, db='poeapi').repl();
cursor = r.table('itemCount').run();
for document in cursor:
        print(document)

