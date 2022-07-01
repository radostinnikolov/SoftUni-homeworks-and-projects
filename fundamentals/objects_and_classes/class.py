class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        result = sum(self.grades) / len(self.grades)
        return float(f'{result:.2f}')

    def __repr__(self):
        student_names = ", ".join(self.students)
        return f"The students in {self.name}: {student_names}. Average grade: {self.get_average_grade()}"

