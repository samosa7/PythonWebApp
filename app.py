from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return " "

@app.route('/stfuanu.html')
def index():
   return "stfuanu sub-tko-poc\n"

@app.route('/stfuanu-storedxss-ato.html')
def homepoc():
   return render_template('stfuanu-storedxss-ato.html')

if __name__ == '__main__':
   app.run()
