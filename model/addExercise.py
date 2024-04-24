from ..app import db, ma

class AddExercise(db.Model):

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id") , primary_key=True)
    duration = db.Column(db.Integer)
    
    def __init__(self, user_id, exercise_id, duration):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.duration = duration

class AddExerciseSchema(ma.Schema):
    class Meta:
        fields = ("user_id", "exercise_id", "duration")
        model = AddExercise
    
add_exercise_schema = AddExerciseSchema()