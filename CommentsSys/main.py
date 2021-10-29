from flask import Flask, render_template, url_for, redirect, request
from pymongo import ALL, MongoClient

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/messages')
def messages():
    client = MongoClient('localhost', 27017)
    db = client['Laiberi']
    collection = db['comments']
    result = list(collection.find({}, {'_id' : False}))
    return render_template('list.html', messages=result)

@app.route('/submit_message', methods=['POST'])
def submit_message():
  message = {'Commenter': request.form['who'],'Message': request.form['message']}

  client = MongoClient('localhost', 27017)
  db = client['Laiberi']
  collection = db['comments']
  collection.insert(message)
  return redirect(url_for('messages'))


if __name__ == "__main__":
    app.run( debug = True )