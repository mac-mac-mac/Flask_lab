import urllib.request, json

from flask import Flask, render_template, request   # import flask framework
app = Flask(__name__)                               # create an app instance

@app.route("/")                                     # use the home url
def hello():                                        # method called hello
    url = "https://xkcd.com/info.0.json"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template("index.html", datum=dict)

@app.route("/<name>")                               # route with URL variable /<name>
def hello_name(name):                               # call method hello_name
    return "Hello "+ name                           # which returns "hello + name

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Mac" 
    return render_template("about.html", aboutName=name) 

if __name__ == "__main__":                          # when running python app.py
    app.run(debug=True)                             # run the flask app