class Student:
    def __init__(self,name,course):
        self.name = name;
        self.course= course;

    @staticmethod
    def hello():
        print("hello !")

s1 = Student("Priti Maurya","Master of computer Application");
s1.hello()      