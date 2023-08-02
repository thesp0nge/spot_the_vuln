from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password123':
        return jsonify({'message': 'Login success'})
    else:
        return jsonify({'message': 'Login failed'})
