from flask import Flask, request, session, redirect

app = Flask(__name__)
app.secret_key = b'secret_key'

@app.route('/login', methods=['POST'])
def login():
    session['user_id'] = request.form['user_id']
    return redirect('/dashboard')

