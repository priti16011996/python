# def Avag(a,b,c):
#     sum = a+b+c;
#     avg=sum/3;
#     print(avg);


# Avag(3,7,6);

# def Mult(a=7,b=4):
#     mult= a*b;
#     print(mult);

# Mult();
# Mult(78,98);
# Mult(5);

# def printLenList(list):
#     print(len(list));

# a=[1,3,5,56,7,75,54,43,33,22];
# printLenList(a);

# def printList(list):
#     for item in list:
#         print(item, end=" \n");

# printList(a);

# def factNum(n):
#     if(n==0 || n==1):
#         return 1;
#     return n*factNum(n-1);

# num = factNum(5);
# print(num);

num = int(input("Enter the number you want to check: "));
def NumType(num):
    if(num%2==0):
        print("eveb");
    elif(num%2==1):
        print("odd");

NumType(num);


