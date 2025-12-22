# bai 1 
a = int ( input ( " nhập một số nguyên bất kỳ " ))
if ( a > 10 and a % 2 == 0 and a % 3 == 0 ):
    print ( a , " là số đúng " )
else :
    print ( a , " là số sai " )
# bai 2
a = 15 - 3 * 4 + 2 ** 3
b = ( 15 - 3 ) * ( 4 + 2 ) ** 3
c = 10 % 3 + 5 // 2 * 4
print ( a )
print ( b )
print ( c )
# bai 3 
total = 100
total -=  25
total *= 2
total /= 5
total += 10
print ( total )
# bai 4
a = "python"
b = "programming"
print ( a not in b )
