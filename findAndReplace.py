with open("sample.txt", "r") as f:
    data = f.read()

data = data.replace("Java", "Python")

with open("sample.txt", "w") as f:
    f.write(data)