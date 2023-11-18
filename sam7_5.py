# написать программу кот-ая будет решать примеры (из 2 переменных) из текстового файла. И выводить результат в этот текстовый файл результат
with open("input7_sam5.txt", "r") as f:
    reader = f.readlines()
with open("input7_sam5.txt", "w") as f:
    for i in reader:
        i.strip()
        i = i.split()
        if i[1] == "+":
            result  = int(i[0]) + int(i[2])
        if i[1] == "-":
            result = int(i[0]) - int(i[2])
        if i[1] == "*":
            result = int(i[0]) * int(i[2])
        if i[1] == "/":
            result = int(i[0]) / int(i[2])
        i.append("=")
        i.append(str(result))
        i.append("\n")
        il = " ".join(i)
        f.write(il)


