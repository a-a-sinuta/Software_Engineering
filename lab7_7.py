lines = ["one", "two", "three"]
with open("input7.txt", "w") as f:
    for line in lines:
        f.write("\nCycle run "+ line)
    print("done")