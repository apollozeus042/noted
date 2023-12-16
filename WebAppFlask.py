from pyngrok import ngrok

# Set your authtoken
authtoken = "2Z7LSq6cLoUL1VVIwPLVFfTtIE8_3Go62c2YHEBoV58DXtS6L"
ngrok.set_auth_token(authtoken)

from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok
import os
import threading
from Database.account_db import selectAcc


app = Flask(__name__)
port = "5000"

public_url = ngrok.connect(port).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

app.config["BASE_URL"] = public_url

app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def demo():
    return render_template('logInPage.html')

@app.route('/signIn', methods=['POST'])
def signIn():
    email = request.form['email']
    password = request.form['password']
    record= selectAcc(email)
    return render_template('logInPage.html', output=f"Name:{record[2]}")

if __name__ == '__main__':
     app.run()