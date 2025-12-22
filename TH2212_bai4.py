a = float(input("hãy nhập số a:"))
b = float(input("hãy nhập số b:"))
c = float(input("hãy nhập số c:"))
def solnnn(a,b,c):
    ln = a
    if b > ln:
        ln = b 
    if c > ln:
        ln = c 
    nn = a
    if b < nn:
        nn = b 
    if c < nn:
        nn = c
    return ln, nn
numMax, numMin = solnnn(a,b,c)
print (f"số lớn nhất là {numMax}")
print (f"Số nhỏ nhất là {numMin}")