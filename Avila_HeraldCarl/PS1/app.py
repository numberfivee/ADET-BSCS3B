from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)