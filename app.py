print ("the day of reckoning is upon us")

from flask import Flask
app = Flask(__name__)

i = 0

@app.route("/")
def index():
    global i
    return "the day of reckoning is upon us" + " " + str(i)

@app.route("/addtwo")
def addone():
    global i 
    i = i + 2
    return "added"

app.run()
