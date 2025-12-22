numbers = [x for x in range(1,10,1) ]
copy_list = numbers.copy()
print(f"{numbers}-> {copy_list} -> {copy_list[::-1]}")