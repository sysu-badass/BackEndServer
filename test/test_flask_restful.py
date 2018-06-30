from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'}
}

USERS = {
    'user1': {'task': 1},
    'user2': {'task': 2},
    'user3': {'task': 3}
}

#经过本次实验，证明parser.parse_args()只会读取当前request中的数据
#并且用对应的key把数据获取

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

def abort_if_user_doesnt_exist(todo_id):
    if todo_id not in USERS:
        abort(404, message="User {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        #return dictionary
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        #str.lstrip(string)作用是将str最前面中含有的第一个string的部分strip掉
        #string左边的也会全部删掉
        todo_id = int(max(TODOS.keys()).lstrip('user')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class User(Resource):
    def get(self, todo_id):
        abort_if_user_doesnt_exist(todo_id)
        return USERS[todo_id]

    def delete(self, todo_id):
        abort_if_user_doesnt_exist(todo_id)
        del USERS[todo_id]
        return '', 204

    def put(self, todo_id):
        #return dictionary
        args = parser.parse_args()
        task = {'task': args['task']}
        USERS[todo_id] = task
        return task, 201

class UserList(Resource):
    def get(self):
        return USERS

    def post(self):
        args = parser.parse_args()
        #str.lstrip(string)作用是将str最前面中含有的第一个string的部分strip掉
        #string左边的也会全部删掉
        todo_id = int(max(USERS.keys()).lstrip('user')) + 1
        todo_id = 'user%i' % todo_id
        USERS[todo_id] = {'task': args['task']}
        return USERS[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
