from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MySQL (using XAMPP)
connection = pymysql.connect(host='localhost', user='root', password='', db='adet')

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        contact_number = request.form['contact_number']
        email = request.form['email']
        address = request.form['address']
        password = request.form['password']
        
        # Hash the password using sha256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        with connection.cursor() as cursor:
            sql = "INSERT INTO adet_user (first_name, middle_name, last_name, contact_number, email, address, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (first_name, middle_name, last_name, contact_number, email, address, hashed_password))
            connection.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with connection.cursor() as cursor:
            # Check if the user exists
            cursor.execute("SELECT * FROM adet_user WHERE email=%s", (email,))
            user = cursor.fetchone()
            
            if user:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == user[7]:
                    # Store the details in the session after successful login
                    session['loggedin'] = True
                    session['first_name'] = user[1]  # First Name
                    session['middle_name'] = user[2]  # Middle Name
                    session['last_name'] = user[3]  # Last Name
                    session['email'] = user[4]  # Email
                    session['contact_number'] = user[5]  # Contact Number
                    session['address'] = user[6]  # Address
                    return redirect(url_for('dashboard'))
                else:
                    flash('Incorrect password. Please try again.', 'error')
            else:
                flash('Email is not registered. Please check your email or sign up.', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        # Create a list of user details from session variables
        user_details = [
            session.get('first_name'),
            session.get('middle_name'),
            session.get('last_name'),
            session.get('contact_number'),
            session.get('email'),
            session.get('address')
        ]
        # Pass the user_details list to the dashboard template
        return render_template('dashboard.html', user_details=user_details)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
