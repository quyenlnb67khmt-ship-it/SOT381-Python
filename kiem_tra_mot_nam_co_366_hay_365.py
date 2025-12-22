nam = int (input ("Hãy nhập năm cần nhận biết: "))
if  nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0:
    print ("Năm nay có 365 ngày")
else:
    print ("Năm nay có 366 ngày")
