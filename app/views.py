from app import app
from flask import render_template, request
import rethinkdb as r

@app.route('/')
@app.route('/index')
def index():
  r.connect('35.166.62.31',28015, db='poeapi').repl();
  cursor = r.table('itemCount').run();
  user = { 'nickname': 'Miguel' } # fake user
  mylist=[1,2,3,4]
  return render_template("index.html", title = 'Home', user = user, mylist = mylist)

@app.route('/realtime')
def realtime():
 return render_template("realtime.html")

@app.route('/r2')
def r2():
 return render_template("r2.html")
