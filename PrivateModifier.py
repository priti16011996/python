class Account:
    def __init__(self,Account_Number,Account_Password):
        self.Account_Number = Account_Number;
        self.__Account_Password = Account_Password;
    def getPassword(self):
        print("Account Password: ",self.__Account_Password);


A1 = Account("12345","!@#DMLkm$");
print(A1.Account_Number)
#print(A1.__Account_Password); # Due to Private it failed to access Password
A1.getPassword();
