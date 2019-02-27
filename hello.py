from flask import Flask
app = Flask(__name__) # create instance of Flask class

@app.route('/') # URL to trigger function
def hello_world():
    return 'Hello world!'

# Run using `FLASK_APP=hello.py flask run` while in the virtualenv. 
# In the browser, go to the address given to see "Hello world!"

# FLASK_APP 
