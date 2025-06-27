import jwt
from datetime import datetime, timedelta

payload = {
    "sub": "1234567890",
    "name": "João Doe",
    "admin": True,
    "iat": datetime.utcnow(),
    "exp": datetime.utcnow() + timedelta(hours=1)
}

SECRET_KEY = "fake_secret"  

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(token)
