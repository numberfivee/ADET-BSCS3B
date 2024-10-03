from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'new_password',  # Replace with your MySQL password
    'database': 'adet'
}

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

        # Save data to MySQL database
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            sql = """
            INSERT INTO adet_user (first_name, middle_name, last_name, birthdate, email, address)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                registration_data['first_name'],
                registration_data['middle_name'],
                registration_data['last_name'],
                registration_data['birthdate'],
                registration_data['email'],
                registration_data['address']
            ))
            conn.commit()
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            return f"Error: {err}"

        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)
