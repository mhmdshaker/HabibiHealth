from ..app import db, ma


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    calories_burnt = db.Column(db.Float, unique=False)
    
    def __init__(self, name, calories_burnt):
        self.name = name
        self.calories_burnt = calories_burnt



class exercise_schema(ma.Schema):
    class Meta:
        fields = ("id", "name", "calories_burnt")
        model = Exercise
Exercise_schema = exercise_schema()
Exercise_schema = exercise_schema(many=True)
