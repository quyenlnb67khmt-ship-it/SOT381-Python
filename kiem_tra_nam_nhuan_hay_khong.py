nam = int(input("Hãy nhập năm bạn muốn kiểm tra:"))
if nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
    print ("Đây là năm nhuận")
else:
    print ("Đây không phải là năm nhuận")