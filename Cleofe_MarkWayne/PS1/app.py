from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to handle form submission
@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f"Hello World! {name}, welcome to CCCS 106 - Applications Development and Emerging Technologies"

if __name__ == '__main__':
    app.run(debug=True)
