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
