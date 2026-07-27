from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Sample E-Commerce Website</h1>
    <p>This website is deployed on Azure App Service.</p>
    <button>Shop Now</button>
    """

if __name__ == "__main__":
    app.run()