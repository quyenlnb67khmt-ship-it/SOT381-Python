danh_sach = [i for i in range(1,20)]
x = int(input("Hãy nhập số cần tìm: "))
tim_x = x in danh_sach
vi_tri_x = danh_sach.index(x)
print (f"Số {x} có trong danh sách đúng không? -> {tim_x}")
print (f"Vị trí của {x} là: {vi_tri_x} ")