from flask import Flask
from routes import home_page

app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET", "POST"])
def render_index():
    return home_page()

if __name__ == "main":
    app.run()