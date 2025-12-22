a = float (input ("Hãy nhập giá trị số a: "))
b = float (input ("Hãy nhập giá trị số b: "))
c = float (input ("Hãy nhập giá trị số c: "))
if a > b > c:
    print ("a là số lớn nhất")
elif b > a > c:
    print ("b là số lớn nhất")
elif c > b > a:
    print ("c là số lớn nhất")
else:
    print ("cả ba số bằng nhau")
    