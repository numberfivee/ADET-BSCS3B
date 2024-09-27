from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')

@app.route('/', methods=['GET', 'POST'])
def my_form():
    if request.method == 'POST':
        text = request.form.get('text', '')
        return 'Hello World! ' + text
    return render_template('html.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
