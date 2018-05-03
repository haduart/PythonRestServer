from flask import Flask, request, jsonify
from services.service import Server
from services.database import Database

database = Database()
server = Server(database)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/foo')
def get_foo():
    raise InvalidUsage('This view is gone', status_code=410)


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
    json_object = request.get_json()
    return server.add_user(json_object)


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