class Lab03:
    def __init__(self, initial_count):
        self.count = initial_count

    def add(self, x):
        self.count += x

    def get_current_count(self):
        return self.count


def main():
    l = Lab03(5)
    l.add(5)
    print(l.get_current_count())
