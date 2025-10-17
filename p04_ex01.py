y = int(input("Nhập năm: "))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f"{y} là năm nhuận.")
else:
    print(f"{y} không phải là năm nhuận.")
