from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   print('Index Triggered')
   return 'The server is up, running, and printing statements'

app.run()