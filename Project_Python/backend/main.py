from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # cho phép gọi từ frontend (http://localhost:...)

def get_db_connection():
    """Kết nối tới file data/data.db bên ngoài thư mục backend."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "..", "data", "data.db")
    return sqlite3.connect(db_path)

@app.route("/api/bookings", methods=["POST"])  # API endpoint để tạo booking thật
def create_booking():
    data = request.get_json() or {}
    print("Received booking:", data)  # xem log trong terminal

    # Các field bắt buộc (trùng với các ô có required trên form)
    required = [
        "room_id",
        "check_in",
        "check_out",
        "guest_name",
        "guest_phone",
        "guest_email",
        "guest_id_card",
    ]
    missing = [k for k in required if k not in data or not data[k]]
    if missing:
        return (
            jsonify(success=False, message=f"Thiếu dữ liệu: {', '.join(missing)}"),
            400,
        )

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Lưu thông tin khách (nếu chưa có) vào bảng customer
        cur.execute(
            "INSERT OR IGNORE INTO customer (name, phone, email, id_card) VALUES (?, ?, ?, ?)",
            (
                data["guest_name"],
                data["guest_phone"],
                data["guest_email"],
                data["guest_id_card"],
            ),
        )

        # Lưu booking (có thêm giờ nhận / trả phòng nếu có)
        cur.execute(
            """
            INSERT INTO booking (
                room_id,
                check_in,
                check_out,
                check_in_time,
                check_out_time,
                guest_name,
                guest_phone,
                guest_email,
                guest_id_card
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["room_id"],
                data["check_in"],
                data["check_out"],
                data.get("check_in_time"),
                data.get("check_out_time"),
                data["guest_name"],
                data["guest_phone"],
                data["guest_email"],
                data["guest_id_card"],
            ),
        )

        # Cập nhật trạng thái phòng thành occupied
        cur.execute(
            "UPDATE room SET status = 'occupied' WHERE id = ?",
            (data["room_id"],),
        )

        conn.commit()
        conn.close()
    except sqlite3.IntegrityError as e:
        return jsonify(success=False, message=f"Lỗi dữ liệu: {e}"), 400
    except Exception as e:
        print("Booking error:", e)
        return jsonify(success=False, message="Lỗi server khi lưu booking"), 500

    return jsonify(success=True, message="Đặt phòng thành công!"), 200

if __name__ == "__main__":
    # chạy đúng port 8000 để khớp với API_BASE_URL trong booking.html
    app.run(host="0.0.0.0", port=8000, debug=True)