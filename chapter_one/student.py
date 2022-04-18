class Student:

    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    def __str__(self):
        return str(self.student_name) + ',' + str(self.marks)


Student_name = "Alexandra"
Student_marks = 80


print(Student_name)
print(Student_marks)
