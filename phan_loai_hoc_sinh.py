diem_so = [8.5, 7.0, 9.2, 6.8, 5.5, 8.8]
for i in range(len(diem_so)):
    if diem_so[i] >= 8.0:
        print ("Bạn đủ điểm học sinh giỏi")
    elif 6.5< diem_so[i] < 7.9:
        print ("Bạn đủ điẻm học sinh khá")
    elif diem_so[i] <6.5:
        print ("Bạn đủ điểm học sinh trung bình")
    else:
        print ("Bạn đạt học dinh yếu")