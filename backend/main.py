from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth, firestore
from datetime import datetime

# Khởi tạo Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    note: str = ""

def verify_token(token: str) -> str:
    """Xác thực Firebase token, trả về uid"""
    try:
        decoded = auth.verify_id_token(token)
        return decoded["uid"]
    except Exception:
        raise HTTPException(status_code=401, detail="Token không hợp lệ")

@app.get("/")
def root():
    return {"message": "Expense API đang chạy"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/expenses")
def add_expense(expense: Expense, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    uid = verify_token(token)
    
    doc = {
        "amount": expense.amount,
        "category": expense.category,
        "note": expense.note,
        "created_at": datetime.utcnow().isoformat(),
        "uid": uid
    }
    db.collection("expenses").document(uid).collection("items").add(doc)
    return {"message": "Đã lưu thành công"}

@app.get("/expenses")
def get_expenses(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    uid = verify_token(token)
    
    docs = db.collection("expenses").document(uid).collection("items")\
             .order_by("created_at", direction=firestore.Query.DESCENDING).stream()
    
    return [doc.to_dict() for doc in docs]