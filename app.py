from flask import Flask, jsonify, request
from flask_cors import CORS
from services.populate_processor import UserService
from database import DATABASE_PATH

app = Flask(__name__)
CORS(app)

@app.route('/signup', methods=['POST'])
def signup():
    
    data = request.get_json()

    new_user = UserService.create(DATABASE_PATH, **data)

    return new_user

@app.route('/login', methods=['POST'])
def login():

    # email = request.args.get('email')
    # password = request.args.get('password')


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