# This is app.py, this is the main file called.
# myproject is the folder name that has the __init__ which runs automatically
from myproject import app
from flask import render_template


@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
