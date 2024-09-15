class Lab03:
    def __init__(self, initial_count):
        self.count = initial_count
        self.students = []

    def add(self, x):
        self.count += x

    def get_current_count(self):
        return self.count

    def read_student_list(self):
        students = input("Enter the list of students seperated by comma: ").split(",")
        self.students.extend(students)
        self.add(len(students))


def main():
    l = Lab03(5)
    l.add(5)
    print(l.get_current_count())
