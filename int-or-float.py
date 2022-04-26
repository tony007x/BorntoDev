import math
n = int(input())
x = math.sqrt(n)
print(x)

if x.is_integer():
    print("Integer")
else:
    print("Float")

