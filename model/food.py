from ..app import db, ma


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    calories = db.Column(db.Integer, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)
    def __init__(self, name, calories):
        super(Food, self).__init__(name=name, calories=calories)


class user_schema(ma.Schema):
 class Meta:
    fields = ("id", "name", "calories")
    model = Food
user_schema = user_schema()