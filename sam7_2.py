with open("input7_sam2.txt", "a", encoding="utf-8") as f:
    tf ="да"
    while tf =="да":
        date = input("Введите дату:")
        category = input("Введите категорию расходов:")
        a = int(input("Сколько потратили:"))
        tf = input("Хотите добавить еще расходы?(да/нет)")
        f.write(f"{date} {category} {a} \n")
with open("input7_sam2.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()
