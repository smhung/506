from flask import Flask
import datetime

app = Flask(__name__)
@app.route('/owner')
def owner():
   return "Hello world from Shine May\n"
@app.route('/datetime')
def timestamp():
   return  str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S\n"))
   #  return "Text"
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)

