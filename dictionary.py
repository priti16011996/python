info ={
    "name":"Priti Maurya",
    "age": 22,
    "Qualification":["B.Sc","MCA"],
    "TechStack":("HTML,CSS,JS,Python"),
    "Marks":{
        "B.Sc": 70,
        "MCA": 80
    }
}

print(info);

print(info.keys())
print(list(info.keys()))
print(info.values())
print(list(info.values()))
print(info.items())
print(list(info.items()))
print(info.get("username"))
print(info.update({"username":"priti123"}))
print(info.get("username"))