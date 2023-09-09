from flask import Flask, render_template      # import flask framework
app = Flask(__name__)                         # create an app instance

@app.route("/")                               # use the home url
def hello():                                  # method called hello
    return render_template("index.html")      # returns "hello world"
if __name__ == "__main__":                    # when running python app.py
    app.run(debug=True)                       # run the flask app

@app.route("/<name>")                         # route with URL variable /<name>
def hello_name(name):                         # call method hello_name
    return "Hello "+ name                     # which returns "hello + name

@app.route("/about")                
def about():                    
    return render_template("about.html")   