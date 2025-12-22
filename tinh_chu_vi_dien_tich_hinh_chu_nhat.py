w = float(input("Hãy nhập độ dài cạnh w của hình chữ nhật: "))
h = float(input("Hãy nhập độ dài cạnh h của hình chữ nhật:"))
while True:
    if 0.0<=w and h<=100.0:
        print ("Số {w} và số {h} đã hợp lệ")
        break
    else:
        print("Số {w} và số {h} không hợp lệ,Xin hãy nhập lại")

chu_vi=(w+h)*2
round(chu_vi,2)
dien_tich=w*h
round(dien_tich,2)
print(f"Chu vi hình chữ nhật là: ({w}+{h})*2={chu_vi}")
print(f"Diện tích hình chữ nhật là: {w}*{h}={dien_tich}")