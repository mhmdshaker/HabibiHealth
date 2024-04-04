from flask import Flask,request,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
import jwt
from flask_cors import cross_origin

from .db_config import DB_CONFIG
#new for mail:
from flask import Flask, request, jsonify, abort, url_for, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer


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

app.config['MAIL_SERVER'] = 'live.smtp.mailtrap.io'  # address
app.config['MAIL_PORT'] = 587  # port
app.config['MAIL_USERNAME'] = 'api'  # user_name
app.config['MAIL_PASSWORD'] = '1d86f429bd4d5ba901d73ee815c77401'  # password
app.config['MAIL_USE_SSL'] = False  # authentication
app.config['MAIL_USE_TLS'] = True  # authentication



s = URLSafeTimedSerializer(SECRET_KEY)
@app.route('/user', methods=['POST'])
def user():
    user_name=request.json["user_name"]
    password=request.json["password"]
    email = request.json["email"]
    
    token = s.dumps(email, salt='email-confirm')
    link = url_for('confirm_email', token=token, _external=True)
    
    # Check if user_name already exists
    user = User.query.filter_by(user_name=user_name).first()
    if user:
        return abort(400, description="User already exists")
    new_user = User(
        user_name=user_name,
        password=password,
        email=email,
        confirmed=False
    )
    db.session.add(new_user)
    db.session.commit()
    
    #for mail verification:
    sender = 'mailtrap@demomailtrap.com'
    receivers = ['mohamadshaker20030320@gmail.com']
    # Create a multipart message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "You are awesome!"
    msg['From'] = sender
    msg['To'] = receivers[0]


    # Create the HTML version of the message
    html = """\
    <p>Congrats for sending test email with Mailtrap! \nIf you are viewing this email in your inbox – the integration works. Now send your email using our SMTP server and integration of your choice!\nGood luck! Hope it works.</p>
    <p><a href="{}">Click here to confirm your email</a></p>
    <!-- ... -->
    """.format(link)
    
    # Attach the plain-text and HTML versions to the message
    msg.attach(MIMEText(html, 'html'))

    with smtplib.SMTP('live.smtp.mailtrap.io', 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('api', '1d86f429bd4d5ba901d73ee815c77401')
        server.sendmail(sender, receivers, msg.as_bytes())
        print("mail sent")

    return jsonify(user_schema.dump(new_user))


@app.route('/confirm_email/<token>', methods=['POST', "GET"])
def confirm_email(token):
    try:
        # Decode the token back into the email
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except:
        abort(400, description="Invalid or expired token")

    # Get the user with this email
    user = User.query.filter_by(email=email).first()

    if not user:
        abort(400, description="User not found")

    # Set the user's confirmed field to True
    user.confirmed = True
    db.session.commit()
    return render_template('homepage.html')











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



