from .student import Student

class MiddleSchoolStudent(Student):

    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def display_transportation_message(self):
        if self.gets_transportation:
            return f"{self.name} uses school transportation."

        return f"{self.name} does not use school transportation."


    def summary(self):
        student_summary = super().summary()

        get_transportation_message = self.display_transportation_message()

        return f"\n".join((student_summary,get_transportation_message))

