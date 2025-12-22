nhap_so_luong_bh = n = int(input("Hãy nhập số lượng bài hát mong muốn:"))
danh_sach_bh = []
for i in range(n):
    ten_bai_hat = input(f"Hãy nhập vào tên bài thứ {i}:")
    danh_sach_bh.append(ten_bai_hat)
for i in range (n):
    ten=danh_sach_bh[i]
    TEN=ten.upper()
    print (f"Bài {i}: {TEN}")
print("Các bài có chữ yêu")
for i in range(n):
    ten=danh_sach_bh[i]
    if (ten.find("yêu")!=-1):
        print(f"Bài {i}: {ten}")
ten_bai_dai_nhat=danh_sach_bh[0]
so_tu_cua_bai_dai_nhat=len(ten_bai_dai_nhat.split())
vi_tri_cua_bai = 0
for i in range(n):
    ten_bai_hat=danh_sach_bh[i]
    so_tu = len(ten_bai_hat.split())
    if so_tu>so_tu_cua_bai_dai_nhat:
        vi_tri_cua_bai=i
        ten_bai_dai_nhat=ten_bai_hat
        so_tu_cua_bai_dai_nhat= so_tu
print (f"bài{i}: {ten_bai_dai_nhat}")
