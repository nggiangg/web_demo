const API_BASE_URL = "https://ten-backend.onrender.com/api";

// Lấy danh sách phòng từ backend
async function loadRooms() {
    try {
        const response = await fetch(`${API_BASE_URL}/rooms`);
        const rooms = await response.json();
        renderRooms(rooms);
    } catch (error) {
        console.error("Lỗi khi tải danh sách phòng:", error);
    }
}

// Render danh sách phòng ra HTML
function renderRooms(rooms) {
    const container = document.getElementById("rooms-container");

    if (rooms.length === 0) {
        container.innerHTML = '<p class="text-center text-muted">Không có phòng nào.</p>';
        return;
    }

    container.innerHTML = rooms.map(room => `
        <div class="col-md-4 mb-4">
            <div class="card border-0 shadow-sm overflow-hidden h-100">
                <img src="${room.image_url}" class="card-img-top" alt="${room.name}">
                <div class="card-body text-center">
                    <h4 class="fw-bold">${room.name}</h4>
                    <p class="text-muted">Diện tích: ${room.area}m² | ${room.view}</p>
                    <h5 style="color: #c5a47e;">${room.price.toLocaleString('vi-VN')} VNĐ / Night</h5>
                    <hr>
                    <button class="btn btn-link text-dark text-decoration-none fw-bold" 
                            onclick="viewRoomDetail(${room.id})">
                        READ MORE <i class="fa fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>
    `).join('');
}

// Xem chi tiết phòng
function viewRoomDetail(roomId) {
    window.location.href = `room-detail.html?id=${roomId}`;
}

// Đặt phòng
async function bookRoom(roomId, checkIn, checkOut, guestName, guestPhone) {
    try {
        const response = await fetch(`${API_BASE_URL}/bookings`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                room_id: roomId,
                check_in: checkIn,
                check_out: checkOut,
                guest_name: guestName,
                guest_phone: guestPhone
            })
        });

        const data = await response.json(); // nhận { success: true, message: "Đặt phòng test OK" }

        if (response.ok && data.success) {
            alert(data.message); // sẽ hiện "Đặt phòng test OK"
        } else {
            alert("Lỗi: " + (data.message || "Đặt phòng thất bại"));
        }
    } catch (error) {
        console.error("Lỗi khi đặt phòng:", error);
        alert("Có lỗi kết nối server");
    }
}

// Tải dữ liệu khi trang load xong
document.addEventListener("DOMContentLoaded", () => {
    loadRooms();
});
////////// test ////////////
// function testBooking() {
//     const today = new Date();
//     const tomorrow = new Date(today);
//     tomorrow.setDate(today.getDate() + 1);

//     const checkIn = today.toISOString().split("T")[0];     // yyyy-mm-dd
//     const checkOut = tomorrow.toISOString().split("T")[0]; // yyyy-mm-dd

//     // room_id = 1 chỉ để test
//     bookRoom(
//         1,
//         checkIn,
//         checkOut,
//         "Khách test",
//         "0123456789"
//     );
// }

////////// test ////////////
