from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            return render_template('my-form.html', greeting=f'Hello, {name}!')
    return render_template('my-form.html')

if __name__ == '_main_':
    app.run(debug=True)