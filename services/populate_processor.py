from database import DATABASE_PATH
from services.create_processor import UserRecord
import csv

FIELDNAMES = ['id', 'name', 'email', 'password', 'age']

class UserService():
    @staticmethod
    def list_all():
        with open(DATABASE_PATH) as repository:
            reader = csv.DictReader(repository)
            return list(reader)

    @staticmethod
    def create(**kwargs):
        user_record = UserRecord(**kwargs)
        with open(DATABASE_PATH, 'a') as repository:
            writer = csv.DictWriter(repository, fieldnames=FIELDNAMES)
            writer.writerow(kwargs)
            return kwargs
