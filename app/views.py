from app import app
from datetime import datetime

@app.route('/owner')
def owner():
   return "Hello world from Shine May\n"
@app.route('/datetime')
def datetime():
   return  datetime.now().strftime("%d/%m/%Y %H:%M:%S\n")


