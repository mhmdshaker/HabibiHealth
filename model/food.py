from ..app import db, ma, bcrypt


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=True)

    def _init_(self, name, calories):
        self.name = name
        self.calories = calories
        
class food_schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "calories")
        model = Food

food_schema = food_schema()