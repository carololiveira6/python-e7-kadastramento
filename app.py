from flask import Flask, jsonify, request
from flask_cors import CORS
from services.populate_processor import UserService
from database import DATABASE_PATH
from werkzeug.security import generate_password_hash

app = Flask(__name__)
CORS(app)

@app.route('/signup', methods=['POST'])
def signup():
    
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    age = request.args.get('age')

    new_user = UserService.create(DATABASE_PATH,
        name=name,
        email=email,
        password=password,
        # password=generate_password_hash(
        #     password, method='pbkdf2:sha512'),
        age=age
        )

    return jsonify(new_user)

@app.route('/login', methods=['POST'])
def login():
   pass

@app.route('/profile/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    pass

@app.route('/profile/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    pass

@app.route('/users', methods=['GET'])
def all_users():
    pass