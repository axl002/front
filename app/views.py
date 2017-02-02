from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  user = { 'nickname': 'Miguel' } # fake user
  mylist = [1,2,3,4]
  return render_template("index.html", title = 'Home', user = user, mylist = mylist)

