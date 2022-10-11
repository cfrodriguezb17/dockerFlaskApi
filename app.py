import firebase_admin
import pyrebase
from firebase_admin import credentials, auth
import json
from flask import Flask, request, jsonify
from functools import wraps
from palindrome import longestPalSubstr

app = Flask(__name__)
cred = credentials.Certificate('fbAdminConfig.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provided.'},400
        return f(*args, **kwargs)
    return wrap

@app.route('/')
def index():
    return jsonify({'message': 'Bienvenido'})

@app.route('/palindromo', methods=['POST'])
@check_token
def resolveText():
    sendText = request.json['text']
    palindromo = longestPalSubstr(sendText)
    return jsonify({'palindromo': palindromo})

@app.route('/signup')
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return {'message': 'Error missing email or password'},400
    try:
        user = auth.create_user(
            email=email,
            password=password
        )

        return {'message': f'Successfully created user {user.uid}'},200
    except:
        return {'message': 'Error creating user'},400

@app.route('/token')
def token():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'},400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')