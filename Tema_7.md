# Тема7. Работа с файлами (ввод, вывод)

----
Отчет по Теме №7 выполнил:

- Синюта Александр Анатольевич
- ПИЭ-21-2

| Задание    | Лаб_раб | Сам_раб |
|------------|---------|------|
| Задание 1  | +       | +    |
| Задание 2  | +       | +    |
| Задание 3  | +       | +    |
| Задание 4  | +       | +    |
| Задание 5  | +       | +    |
| Задание 6  | +       |     |
| Задание 7  | +       |     |
| Задание 8  | +       |     |
| Задание 9  | +       |     |
| Задание 10 | +       |      |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:

- к.э.д., доцент Панов М.А.

## Лабораторная работа №1

-----

### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_1.png)

## Лабораторная работа №2

-----

### 
```python
f = open("input7.txt", "r")
print(f.readline())
f.close()
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_2.png)

## Лабораторная работа №3

-----

### 
```python
f = open("input7.txt", "r")
print(f.readlines())
f.close()
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_3.png)

## Лабораторная работа №4

-----

### 
```python
with open("input7.txt") as f:
    print(f.readlines())
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_4.png)

## Лабораторная работа №5

-----

### 
```python
with open("input7.txt") as f:
    for line in f:
        print(line)
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_5.png)

## Лабораторная работа №6

-----

### 
```python
with open("input7.txt", "a+") as f:
    f.write("\n Im additional line")
with open("input7.txt", "r") as f:
    result = f.readlines()
    print(result)
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_6.png)

## Лабораторная работа №7

-----

### 
```python
lines = ["one", "two", "three"]
with open("input7.txt", "w") as f:
    for line in lines:
        f.write("\nCycle run "+ line)
    print("done")
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_7.png)

## Лабораторная работа №8

-----

### 
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит:")
        print(f"Директории: {', '.join([folder for folder in catalog[1]])}")
        print(f"Файлы: {', '.join([file for file in catalog[2]])}")
        print("-"* 40)


print_docs("G:\Документы\Универ\ооп")
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_8.png)

## Лабораторная работа №9

-----

### 
```python
def longest_words(file):
    with open(file, encoding="utf-8") as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words


print(longest_words("input7_9.txt"))
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_9.png)

## Лабораторная работа №10

-----

### 

```python
import csv
import datetime
import time

with open('rows_300.csv', "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["№", "Секунда", "Микросекунда"])
    for line in range(1,301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/lab7_10.png)

## Самостоятельная работа №1

-----

### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация
```python
f = open("input7_sam1.txt", "r", encoding="utf-8")
reader = f.read()
words = reader.split()
max = 0
for w in words:
    c = words.count(w)
    if c>max:
        max=c
        x = w
print(len(words), x)
f.close()
```
### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_01(2).png)
![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_01.png)

## Выводы

``f = open("input7_sam1.txt", "r", encoding="utf-8")`` - открываем файл с помощью функции open в которую передаем название нашего файла и для чего мы его открываем

``f.close()`` - в конце обязательно не забваем закрыть файл, так как мы воспользовались конструкцией "with open"

``reader = f.read()`` - в этой строке мы считываем все из файла в переменную reader

## Самостоятельная работа №2

-----

### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы
```python
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
```
### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_02.png)


## Выводы

``with open("input7_sam2.txt", "a", encoding="utf-8") as f:`` - в этот раз используем конструкцию "with open", чтобы не писать f.close.В нее передаем файл на добавление так как мы собираемся делать ввести в нем наши расходы

``date = input("Введите дату:")`` - для учета мы будем хранить 3 значения: дату, категорию, затраты. Эти данные мы запрашиваем

`` f.write(f"{date} {category} {a} \n")`` - в этой строке мы добавляем запись в наш файл в котором мы храним наш учет расходов 

``with open("input7_sam2.txt", "r", encoding="utf-8") as f:`` - в этот раз нам надо только считать данные из файла чтобы передать их в консоль, поэтом мы открываем этот же файл но уже на прочтение

## Самостоятельная работа №3

-----

### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
• Текст в файле:

Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

• Ожидаемый результат:

Input file contains:

108 letters

20 words

4 lines
```python
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
```
### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_03.png)


## Выводы

``with open("input7_sam3.txt") as f:`` - когда открываешь файл для чтеня можено не указывать это в параметре, так как этот параметр по умолчанию "r"

`` lines +=1;`` - так как мы считываем наш файл построчно, мы считаем строки просто добавляя +1 каждую итерацию цикла

`` words += len(line.split())`` - слова мы считаем просто каждую строку превращаем в список слов благодаря split, и находим кол-во элементов функцией len 

``line = line.strip(".\n")`` - для подсчета кол-ва букв, нам надо сначала избавиться от лишних символов, а потом подсчитать оставшиеся символы. В этой строке избавились от всех точек

``line = line.replace(" ", "")`` - а в этой строке путем замены пробела на ничего, убрали все пробелы

## Самостоятельная работа №4

-----

### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
• Запрещенные слова:
hello email python the exam wor is
• Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!

• Ожидаемый результат:
*****, ***ld! ****** ** *** programming language of *** future. My
***** **....
****** ** awesome!!!!
```python
sentence = input("Введите предложение:")
li = list(sentence)


with open("input7_sam4.txt", "r") as f:
    words = f.read().split()

sentence_list = sentence.split()
for sw in range(len(sentence_list)):
    word_from_sl = sentence_list[sw].lower()
    for w in words:
        word_from_sl = word_from_sl.replace(w, len(w)*"*")
    sentence_list[sw] = word_from_sl
sentence_l =" ".join(sentence_list)
sli = list(sentence_l)
for x in range(len(sli)):
    if sli[x] == "*":
        li[x] = "*"
print("".join(li))

```
### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_04.png)


## Выводы

``with open("input7_sam4.txt", "r") as f:`` - просто считываем файл с запреткой, чтобы потом из него сделать массив из запрещенных слов

`` for sw in range(len(sentence_list)):`` - в этом цикле мы все слова из предложения записываем в нижнем регистре и ищем в этом слове запрещенный элемент если он есть меняем его на **. Каждое слово добавляем в новый массив.

`` for x in range(len(sli)):`` - в этом цикле мы проходимся по массиву без запрещенки, и если нам встречается *, то в массиве с запрещенкой мы меняем элемент на котором в массиве без запрещенки *, на *. Таким образом не портим регистр в остальных словах

## Самостоятельная работа №5

-----

### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом
```python
# написать программу кот-ая будет решать примеры (из 2 переменных)
# из текстового файла. И выводить результат в этот текстовый файл
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

```
### Результат.

![](https://github.com/a-a-sinuta/Software_Engineering/blob/Tema_7/pic/sam7_04.png)


## Выводы

``with open("input7_sam5.txt", "r") as f:`` - открываем файл для считывания из него примеров

`` reader = f.readlines()`` - для считывания сразу всех строк и добавления их в массив

`` with open("input7_sam5.txt", "w") as f:`` - далее мы открываем наш файл для записи. Сначла он сам удалит все что в нем есть.

`` f.write(il)`` - а потом мы заново напишем наш пример но уже с резульатом
