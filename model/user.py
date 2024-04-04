from ..app import db, ma, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), unique=True)
    hashed_password = db.Column(db.String(128))
    email = db.Column(db.String(50), unique=True)
    confirmed = db.Column(db.Boolean, default=False)
    def __init__(self, user_name, password, email, confirmed):
        super(User, self).__init__(user_name=user_name, email=email, confirmed=confirmed)
        self.hashed_password = bcrypt.generate_password_hash(password)


class user_schema(ma.Schema):
 class Meta:
    fields = ("id", "user_name", "email", "confirmed", "hashed_password")
    model = User
user_schema = user_schema()

