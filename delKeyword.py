class Student:
    def __init__(self,name):
        self.name = name;
    @staticmethod
    def Hello():
        print("Hello Welcome to the Hoggword");

S1 = Student("Raj Maurya");
print(S1.name);
del S1.name;
print(S1.name);
