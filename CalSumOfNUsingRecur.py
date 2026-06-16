num = int(input("Enter the Number you want to calculate: "));

def SumOfN_Num(num):
    if(num ==0):
        return 0;
    return (num + SumOfN_Num(num-1));

print(SumOfN_Num(num));