# from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Jenkins CI Pipeline 🚀"

def insecure_function():
    password = "hardcoded_password"  # security issue
    eval("print('this is unsafe')")  # code smell

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
