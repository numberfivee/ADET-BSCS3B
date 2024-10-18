from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database connection (using XAMPP)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'adet'
}

# Define the home route to display the registration form
@app.route('/')
def registration_form():
    return render_template('register.html')

# Define the route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Get form data
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    contact_number = request.form['contact_number']
    email = request.form['email']
    address = request.form['address']

    # Insert form data into MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO adet_user (first_name, middle_name, last_name, contact_number, email, address)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(insert_query, (first_name, middle_name, last_name, contact_number, email, address))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for('registration_form'))

if __name__ == '__main__':
    app.run(debug=True)
