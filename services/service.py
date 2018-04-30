"""
All the logic that can and should be tested will be here


@author: Eduard Cespedes Borràs
@mail: eduard@iot-partners.com
"""


class Server:

    def __init__(self, database):
        self.db = database

    def get_users(self):
        print("service.py get_users(self)")
        users = self.db.get_users()
        return users

    def add_user(self, json_object):
        username = json_object['username']
        email = json_object['email']

        print("service.py add_user(self)")
        print("service.py username: " + username)
        print("service.py email: " + email)
        added_user = self.db.add_user(username, email)
        return added_user

    def update_user(self, id, username, email):
        print("service.py update_user(self, id, username, email)")
        print("service.py id: " + id)
        print("service.py username: " + username)
        print("service.py email: " + email)
        aupdated_user = self.db.update_user(id, username, email)
        return aupdated_user

    def delete_user(self, id):
        print("service.py delete_user(self, id)")
        print("service.py id: " + id)
        deleted_user = self.db.delete_user(id)
        return deleted_user

