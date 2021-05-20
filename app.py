from flask import Flask, jsonify, request
from flask_cors import CORS
from services.populate_processor import UserService
from database import DATABASE_PATH
import csv, os
from os.path import exists

FIELDNAMES = ['id', 'name', 'email', 'password', 'age']

app = Flask(__name__)
CORS(app)

@app.route('/signup', methods=['POST'])
def signup():
    
    data = request.get_json()

    new_user = UserService.create(DATABASE_PATH, **data)

    return new_user

@app.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    csv_users = UserService.list_all(DATABASE_PATH)
    for user in csv_users:
        if user['email'] == data['email']:
            result = user.pop('password')

            return user

@app.route('/profile/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    
    csv_users = UserService.list_all(DATABASE_PATH)
    update_informations = dict(request.get_json())

    for user in csv_users:
        if int(user['id']) == user_id:
            user.update(update_informations)

            with open(DATABASE_PATH, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(csv_users)

    result = user.pop('password')

    return csv_users, 201

@app.route('/profile/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    
    csv_users = UserService.list_all(DATABASE_PATH)

    if not exists(DATABASE_PATH) or os.stat(DATABASE_PATH).st_size == 0:

        return 'NO CONTENT'

    for user in csv_users:
        if int(user['id']) == user_id:
            csv_users.remove(user)

            with open(DATABASE_PATH, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writeheader()
                writer.writerows(csv_users)

        return 'NO CONTENT', 204

@app.route('/users', methods=['GET'])
def all_users():

    users = []

    if not exists(DATABASE_PATH) or os.stat(DATABASE_PATH).st_size == 0:

        return 'NO CONTENT'

    with open(DATABASE_PATH, 'r') as file:
        reader = csv.DictReader(file)
        for user in reader:
            users.append(user)

    return users, 201