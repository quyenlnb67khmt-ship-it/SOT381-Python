n = int(input("Hãy nhập số n:"))
tong = 0
for i in range(1,n+1,1):
    if i%2==1:
        tong = tong**2 + i**2
        print (f" Tổng của bình phương số lẻ từ 1 đến {n} là {tong}")