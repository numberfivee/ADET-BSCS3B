from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    name = None  
    if request.method == "POST":
        name = request.form.get("username")  
    return render_template("main.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
