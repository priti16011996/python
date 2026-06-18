class Car:
    def __init__(self):
        pass;

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car Stopped..")

class Toyota(Car):
    def __init__(self, brand):
        self.brand= brand;
    def printBrand(self):
        print("Toyota branding");

class BrandType(Toyota):
    def __init__(self, type):
        self.type= type;

C1 = BrandType("Pertrol");
C1.printBrand();
C1.start();
C1.stop();