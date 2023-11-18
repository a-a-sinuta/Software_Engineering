with open("input7_sam3.txt") as f:
    symbols = 0
    words = 0
    lines =0

    line = f.readline()

    while line:
        lines +=1;
        words += len(line.split())
        line = line.strip(".\n")
        line = line.replace(" ", "")
        symbols +=len(line)
        line = f.readline()
print("Input file contains:")
print(f"{symbols} leters \n{words} words \n{lines} lines")