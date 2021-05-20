from flask import Flask, jsonify, request
from services.populate_processor import UserService
from database import DATABASE_PATH

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    pass

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