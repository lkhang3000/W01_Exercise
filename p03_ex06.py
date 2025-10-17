# Nội dung cần ghi
text = "Hôm nay trời đẹp."

# Mã hóa chuỗi thành dạng nhị phân bằng UTF-8
binary_data = text.encode('utf-8')

# Ghi dữ liệu nhị phân vào file output.txt
with open("output.txt", "wb") as f:
    f.write(binary_data)

print("Đã ghi vào file output.txt theo định dạng nhị phân (UTF-8).")
