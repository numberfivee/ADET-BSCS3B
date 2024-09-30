from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Path to JSON file to store the data
JSON_FILE_PATH = "data.json"

# Function to save data to data.json
def write_data_to_json(new_entry):
    # Check if data.json exists, load it; otherwise, create an empty list
    if os.path.exists(JSON_FILE_PATH):
        with open(JSON_FILE_PATH, 'r') as json_file:
            stored_entries = json.load(json_file)
    else:
        stored_entries = []

    # Append the new data entry
    stored_entries.append(new_entry)

    # Save updated data back to data.json
    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(stored_entries, json_file, indent=4)

@app.route('/')
def homepage():
    return redirect(url_for('registration_form'))

@app.route('/register', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        # Get form input data
        given_name = request.form.get('first_name')
        middle_initial = request.form.get('middle_name')
        surname = request.form.get('last_name')
        dob = request.form.get('birthdate')
        email_address = request.form.get('email')
        home_address = request.form.get('address')

        # Data to be saved in JSON
        user_data = {
            'given_name': given_name,
            'middle_initial': middle_initial,
            'surname': surname,
            'dob': dob,
            'email_address': email_address,
            'home_address': home_address
        }

        # Save the data to the JSON file
        write_data_to_json(user_data)

        return "Registration successful!"

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
