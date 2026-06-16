fruits = ["Apple","Mango","Banana","Guava","Watermelon","Orange"];

def listElem(list,idx=0):
    if(idx == len(list)):
        return;
    print(list[idx],end=",");
    return listElem(list,idx+1);

listElem(fruits);