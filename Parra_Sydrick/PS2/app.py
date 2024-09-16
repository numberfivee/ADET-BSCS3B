from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_FILE = 'registrations.json'

# Ensure the file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as file:
        json.dump([], file)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Collect form data
        registration_data = {
            'first_name': request.form.get('first_name'),
            'middle_name': request.form.get('middle_name'),
            'last_name': request.form.get('last_name'),
            'birthdate': request.form.get('birthdate'),
            'email': request.form.get('email'),
            'address': request.form.get('address')
        }
        
        # Save to JSON file
        with open(DATA_FILE, 'r+') as file:
            data = json.load(file)
            data.append(registration_data)
            file.seek(0)
            json.dump(data, file, indent=4)
        
        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration Successful!"

if __name__ == '_main_':
    app.run(debug=True)