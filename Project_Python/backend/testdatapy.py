import sqlite3

# # Đường dẫn tới file database thật trong project
# chỉnh sửa status của phòng 102 thành "occupied" để test booking
# conn = sqlite3.connect("data\\data.db")
# cur = conn.cursor()
# cur.execute(
#     "UPDATE room SET status = ? WHERE room_number = ?",
#     ("occupied", 102),
# )
# conn.commit()
# conn.close()

# Chỉnh sửa tiền price của phòng 101 thành 1500000 để test booking
# Lưu ý: file backend nằm khác thư mục với data, nên dùng "..\\data\\data.db"
# conn = sqlite3.connect("data\\data.db")
# cur = conn.cursor()
# cur.execute(
#     "UPDATE room SET price = ? WHERE room_number = ?",
#     (1500000, 101), # chỉnh sửa giá phòng 101 thành 1500000 để test booking
# )
# conn.commit()
# conn.close()

# Thêm thông tin khách hàng vào bảng customer để test đăng ký khách
# Các cột: id (AUTOINCREMENT), name, phone, email, id_card
# Từ thư mục backend đi lên một cấp rồi vào thư mục data (..\data\data.db)
conn = sqlite3.connect("data\\data.db")
cur = conn.cursor()
cur.execute(
    "INSERT INTO customer (name, phone, email, id_card) VALUES (?, ?, ?, ?)",
    ("Nguyen Xuan Hoang", "076271291", "hoang@gmail.com", "026351124527"),
)
conn.commit()
conn.close()