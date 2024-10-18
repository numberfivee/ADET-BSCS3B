from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Define the home route to display the registration form
@app.route('/')
def registration_form():
    return render_template('register.html')

# Define the route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    data = {
        'first_name': request.form['first_name'],
        'middle_name': request.form['middle_name'],
        'last_name': request.form['last_name'],
        'contact_number': request.form['contact_number'],
        'email': request.form['email'],
        'address': request.form['address']
    }

    # Save form data to JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    return redirect(url_for('registration_form'))

if __name__ == '__main__':
    app.run(debug=True)
