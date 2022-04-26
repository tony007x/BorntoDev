isint = []
isstr = []
print("พิมพ์ 00 เพื่อออกจาก Loop")
while True:
    n = input("ป้อนค่า: ")
    if n.isdigit() and n!='00':
        isint.append(n)
    elif not n.isdigit() and n!='00':
        isstr.append(n)
    if n =='00':
        break
print("end")
print("ตัวเลข", isint)
print("ข้อความ",isstr)
