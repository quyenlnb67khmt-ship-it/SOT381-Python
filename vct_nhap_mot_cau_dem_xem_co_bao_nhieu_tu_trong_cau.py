def dem_tu(van_ban):
    tu = van_ban.split()
    return len(tu)

van_ban = input("Hãy nhập câu bạn muốn đếm từ:")
print (f"Số từ: {dem_tu(van_ban)}")