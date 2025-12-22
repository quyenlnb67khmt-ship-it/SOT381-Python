so_luong = [15, 8, 22, 5, 12, 3]
ten_san_pham = ["Áo", "Quần", "Giày", "Túi", "Mũ", "Ví"]
for i in range(len(ten_san_pham)):
    if so_luong[i] < 10:
        print (f"Sản phẩm cần nhập thêm:{ten_san_pham[i]}")
    else:
        print (f"Sản phẩm {ten_san_pham[i]} số lượng đã đủ")