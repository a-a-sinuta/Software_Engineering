with open("input7.txt", "a+") as f:
    f.write("\n Im additional line")
with open("input7.txt", "r") as f:
    result = f.readlines()
    print(result)