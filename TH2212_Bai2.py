a = float(input("Hãy nhập số a:"))
b = float(input("Hãy nhập số b:"))
c = float(input("Hãy nhập số c:"))
max = a
if b>max:
    max = b
if c > max:
    max = c

min = a
if b < min:
    min = b
if c < min:
    min = c
print(f"Max: {max}, Min:{min}")