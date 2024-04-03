from ..app import db, ma


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    calories = db.Column(db.Float, unique=False)
   
    def __init__(self, name, calories):
        super(Food, self).__init__(name=name, calories=calories)


class food_schema(ma.Schema):
 class Meta:
    fields = ("id", "name", "calories")
    model = Food
food_schema = food_schema()