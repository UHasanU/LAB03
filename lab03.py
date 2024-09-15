import random


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

    def get_random_groups(self, number_of_students):
        groups = []
        number_of_groups = self.count // number_of_students
        for _ in range(number_of_groups):
            group = []
            while len(group) < number_of_students:
                if random.choice(self.students) not in group:
                    group.append(random.choice(self.students))
            groups.append(group)
        return groups


def main():
    l = Lab03(0)
    l.read_student_list()
    print(l.get_random_groups(2))


main()
