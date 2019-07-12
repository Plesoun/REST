from flask import Flask, render_template


app = Flask.App(__name__, specification_dir="./")


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
