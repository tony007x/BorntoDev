txt = input()
vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
for i in txt:
    if i in vowel:
        txt = txt.replace(i,"")
print(txt)