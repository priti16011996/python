# Print number from 1 to 100 using while loop and then print number from 100 to 1 with decrement of 10 using while loop.
count = 1;
while count<=100:
    print(count)
    count+=1

count =100
while count>=1:
    print(count)
    count-=1

#print multiplication teable of n using while loop
n = int(input("Enter a number to print its multiplication table: "))
i=1;
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1    

#Print list using while loop
list = [1,4,9,16,25,45,76,89,25,63,85]
i=0
while i<=len(list)-1:
    print(list[i])
    i+=1
    
#Search for an element in the touple using while loop
list = [1,4,9,16,25,45,76,89,25,63,85]
n = int(input("Enter a number "))
i=0
while i<=len(list)-1:
    if(list[i]==n):
        print("Element found at index ",i)
        break;
    i+=1
