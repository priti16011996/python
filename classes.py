class Student:
    CollegeName ="Institute of Engineering and Technology,Lucknow"; #Class Attribute
    Course="Master of Computer Application";#Class Attribute
    name="Anonymous"; #Class Attribute
    # default constructor
    def __init__(self):
        pass

    #Parametrize constructor
    def __init__(self,name,marks):
        self.name =name; #Instance Attribute > Class Attribute
        self.marks=marks;

s1 = Student("Priti Maurya",97)
print(s1.name, s1.marks);

s2= Student("Raj Hans Maurya",99);
print(s2.name,s2.marks);