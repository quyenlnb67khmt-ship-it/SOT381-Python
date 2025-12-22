numbers = [2,5,4,7,8,6,9,1,0]
so_chan = [i for i in numbers if i%2==0]
so_le = [i for i in numbers if i%2!=0]
dem_so_chan = len(so_chan)
dem_so_le = len(so_le)
print(f"Số chẵn: {dem_so_chan}")
print(f"Số lẻ: {dem_so_le}")