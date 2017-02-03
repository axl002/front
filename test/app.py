# In this example we are going to create a simple HTML
# page with 2 input fields (numbers), and a link.
# Using jQuery we are going to send the content of both
# fields to a route on our application, which will
# sum up both numbers and return the result.
# Again using jQuery we'l show the result on the page


# We'll render HTML templates and access data sent by GET
# using the request object from flask. jsonigy is required
# to send JSON as a response of a request

from flask import Flask, render_template, request, jsonify
import rethinkdb as r

# Initialize the Flask application
app = Flask(__name__)


# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')

# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/_add_numbers')
def add_numbers():
    r.connect('35.166.62.31',28015, db='poeapi').repl()
    a = request.args.get('a', 'Viridian Jewel', type=str)
    b = request.args.get('b', 0, type=int)

    cursor = r.table('itemCount').filter(r.row["itemName"] == a).run()
    mylist = []
    counter = 0
    for item in cursor:
    	mylist.append(item)
	counter = counter +1
    #return jsonify(result=a + b)
    return jsonify(result = mylist[counter-1])

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )

