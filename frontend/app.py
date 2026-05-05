import streamlit as st
import requests
import json

BACKEND_URL = "http://localhost:8000"
FIREBASE_API_KEY = "ĐIỀN_API_vÀO_ĐÂY"

def login_with_email(email, password, api_key):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    res = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})
    return res.json()

def register_with_email(email, password, api_key):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={api_key}"
    res = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True})
    return res.json()

st.title("💰 Quản lý chi tiêu")

# --- Chưa đăng nhập ---
if "token" not in st.session_state:
    tab1, tab2 = st.tabs(["Đăng nhập", "Đăng ký"])

    with tab1:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Mật khẩu", type="password")
            if st.form_submit_button("Đăng nhập"):
                result = login_with_email(email, password, FIREBASE_API_KEY)
                if "idToken" in result:
                    st.session_state.token = result["idToken"]
                    st.session_state.email = result["email"]
                    st.rerun()
                else:
                    st.error("Sai email hoặc mật khẩu!")

    with tab2:
        with st.form("register_form"):
            email = st.text_input("Email")
            password = st.text_input("Mật khẩu", type="password")
            if st.form_submit_button("Đăng ký"):
                result = register_with_email(email, password, FIREBASE_API_KEY)
                if "idToken" in result:
                    st.success("Đăng ký thành công! Hãy sang tab Đăng nhập.")
                else:
                    msg = result.get("error", {}).get("message", "Không rõ lỗi")
                    st.error(f"Lỗi: {msg}")

# --- Đã đăng nhập ---
else:
    st.success(f"Xin chào: {st.session_state.email}")
    if st.button("Đăng xuất"):
        del st.session_state.token
        del st.session_state.email
        st.rerun()

    headers = {"Authorization": f"Bearer {st.session_state.token}"}

    # --- Thêm chi tiêu ---
    st.subheader("➕ Thêm khoản chi")
    with st.form("add_expense"):
        amount = st.number_input("Số tiền (K)", min_value=0)
        category = st.selectbox("Danh mục", ["Ăn uống", "Đi lại", "Mua sắm", "Giải trí", "Khác"])
        note = st.text_input("Ghi chú")
        if st.form_submit_button("Lưu"):
            res = requests.post(f"{BACKEND_URL}/expenses",
                                json={"amount": amount, "category": category, "note": note},
                                headers=headers)
            if res.status_code == 200:
                st.success("Đã lưu!")
            else:
                st.error("Lỗi!")

    # --- Danh sách chi tiêu ---
    st.subheader("📋 Danh sách chi tiêu")
    res = requests.get(f"{BACKEND_URL}/expenses", headers=headers)
    if res.status_code == 200:
        expenses = res.json()
        if expenses:
            for e in expenses:
                st.write(f"**{e['category']}** — {e['amount']:,.0f}K — {e.get('note', '')} — {e['created_at'][:10]}")
        else:
            st.info("Chưa có khoản chi nào!")
