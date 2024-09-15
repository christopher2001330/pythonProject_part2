class Human:
    head = True

    def say_hello(self):
        print("Здравствуйте")


class Student(Human):
    head = False

    def about(self):
        print("Я студент")

    def say_hello(self):
        print("Здравствуйте")


class Teacher(Human):
    pass


# human = Human()
student = Student()
teacher = Teacher()
student.say_hello()
teacher.say_hello()
print(student.head)
