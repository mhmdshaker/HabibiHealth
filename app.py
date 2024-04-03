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



