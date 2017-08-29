from model import User
from model import Group
from flask import Flask, request, render_template
from persistence_service import PersistenceService
from flask import jsonify
from http import HTTPStatus

app = Flask(__name__)

persistence_service = PersistenceService()

users_endpoint_name = '/user'
groups_endpoint_name = '/group'


@app.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8000'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE'
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route(users_endpoint_name)
def user_list():
    users = persistence_service.load_users()
    return jsonify([u.get_fields() for u in users])


@app.route(users_endpoint_name, methods=['POST'])
def new_user():
    user_data = request.get_json()
    user = persistence_service.save_user(user=User(name=user_data['name'], email=user_data['email']))
    return jsonify(user.get_fields()), HTTPStatus.CREATED.value


@app.route(users_endpoint_name + '/<int:user_id>')
def user_details(user_id):
    usr = persistence_service.load_user(user_id)
    return jsonify(usr.get_fields())


@app.route(users_endpoint_name + '/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    persistence_service.del_user(user_id)
    return ''


@app.route(groups_endpoint_name)
def group_list():
    groups = persistence_service.load_groups()
    return jsonify([g.get_fields() for g in groups])


@app.route(groups_endpoint_name, methods=['POST'])
def new_group():
    group = persistence_service.save_group(group=Group(name=request.get_json()['name']))
    return jsonify(group.get_fields()), HTTPStatus.CREATED.value


@app.route(groups_endpoint_name + '/<int:group_id>')
def group_details(group_id):
    group = persistence_service.load_group(group_id)
    return jsonify(group.get_fields())


@app.route(groups_endpoint_name + '/<int:group_id>', methods=['DELETE'])
def delete_details(group_id):
    persistence_service.del_group(group_id=group_id)
    return ''


@app.route(users_endpoint_name + '/<int:user_id>' + groups_endpoint_name)
def get_users_groups(user_id):
    user = persistence_service.load_user(user_id=user_id)
    return jsonify([{'groupId': g.id} for g in user.groups])


@app.route(users_endpoint_name + '/<int:user_id>' + groups_endpoint_name, methods=['POST'])
def add_users_group(user_id):
    persistence_service.save_users_group(user_id=user_id, group_id=request.get_json()['groupId'])
    return '', HTTPStatus.CREATED.value


@app.route(users_endpoint_name + '/<int:user_id>' + groups_endpoint_name + '/<int:group_id>', methods=['DELETE'])
def delete_users_group(user_id, group_id):
    persistence_service.del_users_group(user_id=user_id, group_id=group_id)
    return ''
