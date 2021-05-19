from flask import Flask, jsonify, request
from services.populate_processor import UserService

app = Flask(__name__)

@app.route('/signup')
def signup():
    pass

@app.route('/login')
def login():
    pass

@app.route('/profile/<int:user_id>')
def update_user(user_id):
    pass

@app.route('/profile/<int:user_id>')
def delete_user(user_id):
    pass

@app.route('/users')
def all_users():
    pass