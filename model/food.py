from ..app import db, ma, bcrypt


class Food(db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Integer, nullable=True)
    protein = db.Column(db.Float, nullable=True)
    fat = db.Column(db.Float, nullable=True)
    carbohydrates = db.Column(db.Float, nullable=True)

    def __init__(self, name, description, price, calories, protein, fat, carbohydrates):
        self.name = name
        self.description = description
        self.price = price
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates
        

class food_schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "price", "calories", "protein", "fat", "carbohydrates")
        model = Food

food_schema = food_schema()