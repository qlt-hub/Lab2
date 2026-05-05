# 💰 Expense App — Quản Lý Chi Tiêu Cá Nhân

Ứng dụng quản lý chi tiêu cá nhân được xây dựng với **FastAPI** (backend), **Streamlit** (frontend) và **Firebase** (Authentication + Firestore Database).

---

## 📁 Cấu trúc dự án

```
PRJ-LAB2/
├── backend/
│   ├── main.py               # FastAPI backend
│   └── requirements.txt      # Thư viện backend
├── frontend/     # API key (không push lên GitHub)
│   ├── app.py
│   └── requirements.txt      # Thư viện frontend
├── .gitignore
└── README.md
```

---

## ⚙️ Cài đặt môi trường

### Yêu cầu

- Python 3.10+
- Git

### Clone dự án

```bash
git clone https://github.com/qlt-hub/Lab2.git
cd Lab2
```

### Cài đặt Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Cài đặt Frontend

```bash
cd frontend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔧 Cấu hình Firebase

### 1. Tạo Firebase Project

- Vào [console.firebase.google.com](https://console.firebase.google.com)
- Tạo project mới
- Bật **Authentication** → Email/Password
- Bật **Firestore Database** → Start in test mode

### 2. Cấu hình Backend

- Vào **Project Settings → Service accounts → Generate new private key**
- Tải file JSON về, đổi tên thành `serviceAccountKey.json`
- Đặt vào thư mục `backend/`

### 3. Cấu hình Frontend

- Vào **Project Settings → General → Your apps → Web app**
- Copy `apiKey`

---

## 🚀 Chạy Backend

```bash
cd backend
.venv\Scripts\activate
uvicorn main:app --reload
```

Backend chạy tại: `http://localhost:8000`

### Các endpoint

| Method | Endpoint    | Mô tả                  |
| ------ | ----------- | ---------------------- |
| GET    | `/`         | Kiểm tra API           |
| GET    | `/health`   | Kiểm tra trạng thái    |
| POST   | `/expenses` | Thêm khoản chi tiêu    |
| GET    | `/expenses` | Lấy danh sách chi tiêu |

---

## 🖥️ Chạy Frontend

```bash
cd frontend
.venv\Scripts\activate
streamlit run app.py
```

Frontend chạy tại: `http://localhost:8501`

---

## ✨ Tính năng

- **Đăng ký** tài khoản mới bằng Email/Password
- **Đăng nhập** bằng Firebase Authentication
- **Đăng xuất** khỏi ứng dụng
- **Thêm khoản chi** với danh mục và ghi chú
- **Xem danh sách** chi tiêu đã lưu
- Dữ liệu được lưu riêng theo từng người dùng trên **Firestore**

---

## 🎥 Video Demo

[Link video demo](https://your-video-link-here)

---

## 👨‍💻 Tác giả

- **Họ tên:** Nguyễn Đại Hiếu
- **MSSV:** 24120180
- **Môn học:** Tư Duy Tính Toán
- **Giảng viên:** Lê Đức Khoan
