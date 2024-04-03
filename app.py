from flask import Flask,request,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
import jwt
from flask_cors import cross_origin

from .db_config import DB_CONFIG

SECRET_KEY = "b'|\xe7\xbfU3`\xc4\xec\xa7\xa9zf:}\xb5\xc7\xb9\x139^3@Dv'"
from datetime import timedelta
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONFIG
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
CORS(app)
db = SQLAlchemy(app)

from .model.user import User, user_schema 
from .model.food import Food, food_schema
from .model.exercise import Exercise, exercise_schema

@app.route('/user', methods=['POST'])
def user():
    user_name=request.json["user_name"]
    password=request.json["password"]
    # Check if user_name already exists
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return abort(400, description="User already exists")
    new_user = User(
        user_name=user_name,
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user))


def create_token(user_id):
    payload = {
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=4),
    'iat': datetime.datetime.utcnow(),
    'sub': user_id
    }
    return jwt.encode(
    payload,
    SECRET_KEY,
    algorithm='HS256'
    )

@app.route('/authentication', methods=['POST'])
def authentication():
    user_name=request.json["user_name"]
    password=request.json["password"]

    if not user_name or not password:
        return abort(400)
    user=User.query.filter_by(user_name=user_name).first()
    if user is None:
        return abort(403)
    if not bcrypt.check_password_hash(user.hashed_password,password):
        return abort(403)
    else:
        return jsonify(
            {"token":create_token(user.id)}
        )
    
def extract_auth_token(authenticated_request):
    auth_header = authenticated_request.headers.get('Authorization')
    if auth_header:
        return auth_header.split(" ")[1]
    else:
        return None

def decode_token(token):
    payload = jwt.decode(token, SECRET_KEY, 'HS256')
    return payload['sub']



