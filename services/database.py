"""
Database logic


@author: Eduard Cespedes Borràs
@mail: eduard@iot-partners.com
"""


class Database:

    def __init__(self):
        self.storage = {}

    def get_users(self):
        print("database.py get_users(self)")
        return "server get_users"

    def add_user(self, username, email):
        print("database.py add_user(self)")
        print("database.py username: " + username)
        print("database.py email: " + email)
        self.storage[username] = email
        return "server add_user"

    def update_user(self, id, username, email):
        print("database.py update_user(self, id, username, email)")
        print("database.py id: " + id)
        print("database.py username: " + username)
        print("database.py email: " + email)
        self.storage[username] = email
        return "server update_user"

    def delete_user(self, id):
        print("database.py delete_user(self, id)")
        print("database.py id: " + id)
        return "server delete_user"
