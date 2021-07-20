# Set up your imports and your flask app.
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('index.html')

# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    username = request.args.get('username')

    upper = lower = number = False

    lower = any(c.islower() for c in username)
    upper = any(c.isupper() for c in username)
    number = username[-1].isdigit()

    # Return the information to the report page html.
    return render_template('report.html', upper=upper, lower=lower, number=number)

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
