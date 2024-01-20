from flask import Flask, render_template, request, redirect

app = Flask(__name__,static_url_path='/static/')



@app.route("/")
def main():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def service():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
