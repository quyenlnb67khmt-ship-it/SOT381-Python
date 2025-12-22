a = int (input ("Hãy nhập giá trị của a:"))
b = int (input ("Hãy nhập giá trị của b:"))
c = int (input ("Hãy nhập giá trị của c:"))
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print ("Đây là tam giác vuông")
elif a**2 + b**2 < c**2 and c > a and c > b:
    print ("Đây là tam giác tù")
elif a**2 + b**2 > c**2 and c > a and c > b:
    print ("Đây là tam giác nhọn")
else:
    print ("Không thuộc ba tam giác trên")