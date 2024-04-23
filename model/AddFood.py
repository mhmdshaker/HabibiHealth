from ..app import db, ma

class AddFood(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    #i just want the user to know what food he has in his cart:
    def _init_(self, user_id, food_id, quantity):
        super(AddFood, self)._init_(user_id=user_id, food_id=food_id, quantity=quantity)
        
class AddFoodSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "food_id", "quantity")
        model =AddFood