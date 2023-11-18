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