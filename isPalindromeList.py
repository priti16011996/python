list=[1,2,3,2,5]
listCopy = list.copy()
listCopy.reverse()
if(list == listCopy):
    print("the list is a palindrome")
else:
    print("the list is not a palindrome")
