# Problem Statement
# Create Account class with two attribute - balance and account number And 
# Create method 
# for debit, credit and printing the balance

class Account:
    def __init__(self, balance,account_no):
        self.balance = balance;
        self.account_no = account_no;

    def debit(self, amount):
        self.balance -= amount;
        print("Amount is debited:",amount);
        print("Now Balance:", self.printBalance());
    
    def credit(self, amount):
        self.balance += amount;
        print("Amount is credited:",amount);
        print("Now Balance:", self.printBalance());

    def printBalance(self):
        return self.balance;

acc1 = Account(25000,123456);
acc1.debit(8500);
acc1.credit(74000);
