from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Path to JSON file to store the data
DATA_FILE = "data.json"

# Function to save data to data.json
def save_to_json(data):
    # Check if data.json exists, load it; otherwise, create an empty list
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    # Append new data
    existing_data.append(data)

    # Save updated data back to data.json
    with open(DATA_FILE, 'w') as file:
        json.dump(existing_data, file, indent=4)

@app.route('/')
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        last_name = request.form.get('last_name')
        birthdate = request.form.get('birthdate')
        email = request.form.get('email')
        address = request.form.get('address')

        # Data to be saved in JSON
        form_data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'birthdate': birthdate,
            'email': email,
            'address': address
        }

        # Save data to JSON file
        save_to_json(form_data)

        return "Registration successful!"

    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
