# Abstraction- Hiding the implementation Details and showing only essentials details to user
class Car:
    def __init__(self):
        self.acc = False;
        self.clutuch = False;
        self.brk= False;

    def start(self):
        self.acc= True;
        self.clutuch= True;
        print("Car Started...");

c1 = Car();
c1.start();