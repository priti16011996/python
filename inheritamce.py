#Inheritance - Single Level Inheritance 
class A:
    def __init__(self):
        pass;

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped..");

class B(A):
    def __init__(self,brand):
        self.brand = brand;

a1 = B("Toyota");
a1.start();
a1.stop();
print(a1.brand);

