import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException

SECRET_KEY = "secret-a8d93b5c1f0e4ce9f2a1c4d5e"
ALGORITHM = "HS256"

def create_token(username: str):
    expire = datetime.now() + timedelta(minutes=30)
    payload = {
        "sub": username,
        "exp": expire
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

#def verify_token(token):
#    payload = jwt.decode(
#        token,
#        SECRET_KEY,
#        algorithms=["HS256"]
#    )
#    return payload

def verify_token(token: str): # (พารามิเตอร์อาจจะต่างไปตามที่คุณเขียนไว้)
    try:
        # บรรทัดนี้คือโค้ดเดิมของคุณ
        payload = jwt.decode(
            token,
            SECRET_KEY, # ใช้ชื่อตัวแปรตามที่คุณมี
            algorithms=["HS256"]
        )
        return payload

    # เพิ่มการดักจับ Error ตรงนี้ครับ
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired. Please log in again."
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token."
        )




