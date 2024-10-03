from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

def save_to_json(data):
    json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'main.json')
    
    if os.path.exists(json_file_path):
        if os.path.getsize(json_file_path) > 0:
            with open(json_file_path, 'r') as json_file:
                existing_data = json.load(json_file)
        else:
            existing_data = []
    else:
        existing_data = []
    
    existing_data.append(data)
    
    with open(json_file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        contact_number = request.form['contact_number']
        email_address = request.form['email_address']
        address = request.form['address']

        data = {
            'first_name': first_name,
            'middle_name': middle_name,
            'last_name': last_name,
            'contact_number': contact_number,
            'email_address': email_address,
            'address': address
        }

        save_to_json(data)
        
        return redirect(url_for('register'))

    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
