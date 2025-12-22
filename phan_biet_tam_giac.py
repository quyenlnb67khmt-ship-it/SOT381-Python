canh_a = a = float(input("Hãy nhập độ dài cạnh a: "))
canh_b = b = float(input("Hãy nhập đồ dài cạnh b: "))
canh_c = c = float(input("Hãy nhập dộ dài cạnh c: "))
if a == b == c:
    print ("Đây là tam giác đều")
elif a == b !=c or a == c != b or b == c != a:
    print ("Đây là tam giác cân")
elif a == b or b == c or a == c and a**2 + b**2 == c**2:
    print ("Đây là tam giác vuông cân")
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print ("Đây là tam giác vuông")
elif a + b > c or a + c > b or b + c > a:
    print ("Đây là tam giác thường")
else:
    print ("Đây không phải là tam giác")
    
    
