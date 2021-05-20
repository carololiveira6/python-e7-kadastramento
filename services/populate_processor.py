from database import DATABASE_PATH
import csv, os
from os.path import exists

FIELDNAMES = ['id', 'name', 'email', 'password', 'age']

class UserService():

    @staticmethod
    def list_all(DATABASE_PATH):

        with open(DATABASE_PATH) as repository:
            reader = csv.DictReader(repository)
            return list(reader)

    @staticmethod
    def get_last_id(DATABASE_PATH):

        id_list = []

        with open(DATABASE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for user in reader:
                id_list.append(int(user['id']))

            if id_list != []:
                my_last_id = sorted(id_list)[-1] + 1
            else :
                my_last_id = 1

            return my_last_id

        # return sorted(id_list)[-1] + 1 if id_list != [] else 1

    @staticmethod
    def create(DATABASE_PATH, **kwargs):

        if not exists(DATABASE_PATH) or os.stat(DATABASE_PATH).st_size == 0:

            with open(DATABASE_PATH, 'w') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

                writer.writeheader()

        # user = dict(request.get_json())
        # user['id'] = get_last_id(DATABASE_PATH)

        my_id = UserService.get_last_id(DATABASE_PATH)

        with open(DATABASE_PATH, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            kwargs['id'] = my_id
            if file.tell() == 0:
                writer.writeheader()
            if UserService.verify_email_exists(DATABASE_PATH, **kwargs):
                return ('', 422)

            writer.writerow(kwargs) 
                
        return (kwargs, 201)

    @staticmethod
    def verify_email_exists(DATABASE_PATH,**kwargs):

        csv_users = UserService.list_all(DATABASE_PATH)

        for user in csv_users:
            if user['email'] == kwargs['email']:
                return True
            
        return False