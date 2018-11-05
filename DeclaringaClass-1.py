class ExerciseSession:
    def __init__(self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration

    def get_exercise(self):
        return self.exercise

    def set_exercise(self, newexercise):
        self.exercise = newexercise

    def get_intensity(self):
        return self.intensity

    def set_intensity(self, newintensity):
        self.intensity = newintensity

    def get_duration(self):
        return self.duration

    def set_duration(self, newduration):
        self.duration = newduration

    def calories_burned(self):
        calories = 0
        if self.intensity == 'Low':
            calories = self.duration* 4
        elif self.intensity == 'Medium':
            calories = self.duration * 8
        elif self.intensity == 'High':
            calories = self.duration * 12
        else:
            raise Exception
        return calories

new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())

