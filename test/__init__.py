from flask import Flask
app = Flask(__name__)
from app import app


#r.connect('35.166.62.31',28015, db='poeapi').repl();
#cursor = r.table('itemCount').run();
#for document in cursor:
#        print(document)
