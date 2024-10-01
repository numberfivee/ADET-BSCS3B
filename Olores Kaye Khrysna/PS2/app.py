from flask import Flask, render_template, request, redirect, jsonify
import json

app = Flask(__name__)

# Function to save data to JSON file
def save_to_json(data):
    try:
        with open('data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    existing_data.append(data)

    with open('data.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])
def register():
    # Collect data from the form
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    birthdate = request.form['birthdate']
    email = request.form['email']
    address = request.form['address']

    # Create a dictionary of the user's data
    user_data = {
        'First Name': first_name,
        'Middle Name': middle_name,
        'Last Name': last_name,
        'Birthdate': birthdate,
        'Email Address': email,
        'Address': address
    }

    # Save the data to a JSON file
    save_to_json(user_data)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
