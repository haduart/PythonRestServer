from flask import Flask, request, jsonify
from services.service import Server
from services.database import Database

database = Database()
server = Server(database)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# curl http://localhost:5000/user
@app.route("/user", methods=["GET"])
def get_user():
    # all_users = User.query.all()
    # result = users_schema.dump(all_users)
    print("app.py get_user")
    return server.get_users()


# curl --header "Content-Type: application/json" --request POST --data '{"username":"Eduard","email":"ed@mail.com"}'
# http://localhost:5000/user
@app.route("/user", methods=["POST"])
def add_user():
    print("app.py add_user")
    username = request.json['username']
    print("app.py username: " + username)
    email = request.json['email']
    print("app.py email: " + email)

    return server.add_user(username, email)


# curl --header "Content-Type: application/json" --request PUT --data '{"username":"Eduard","email":"ed@mail.com"}'
# http://localhost:5000/user/1
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    print("app.py user_update")
    print("app.py id: " + id)
    username = request.json['username']
    print("app.py username: " + username)
    email = request.json['email']
    print("app.py email: " + email)

    return server.update_user(id, username, email)


# curl --header "Content-Type: application/json" --request DELETE http://localhost:5000/user/1
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    print("app.py user_delete")
    print("app.py id: " + id)
    return server.delete_user(id)


if __name__ == '__main__':
    app.run(debug=True)