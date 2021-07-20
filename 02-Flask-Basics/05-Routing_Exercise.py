# Set up your imports here!
# import ...
from flask import Flask, request
app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome to Puppy Latin <br> Go to /puppy_latin/puppy name<h1>'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] == 'y':
        return f"Hi, {name}, your puppy latin name is {name[:-1]+'iful'}"
    return f"Hi, {name}, your puppy latin name is {name+'y'}"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
