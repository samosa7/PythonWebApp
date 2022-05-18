from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return " "

@app.route('/stfuanu.html')
def index():
   return "stfuanu sub-tko-poc\n"

if __name__ == '__main__':
   app.run()
