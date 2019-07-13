import sqlite3
from flask_restful import Resource, reqparse
from models.userModel import User

class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('new_password',
                        type=str
                        )


    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
    def delete(self):
        data = UserRegister.parser.parse_args()
        return(User.delete_from_db(data["username"], data["password"]))
    def put(self):
        data = UserRegister.parser.parse_args()
        return(User.update_in_databse(data["username"], data["password"], data["new_password"]))
