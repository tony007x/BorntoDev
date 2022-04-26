n = int(input())
box = []
pos = []
while True:
    number = input()
    box.append(number)
    if len(box) == n:
        break
j = input()
for i in range(0,len(box)):
    if box[i]==j:
        pos.append(i+1)
    i+=1
op = ','.join(map(str,pos))
print("Position:",op)