import secrets
import jwt
import motor.motor_asyncio
from fastapi import Depends, HTTPException, status
import bcrypt
from fastapi.security import HTTPBasicCredentials, HTTPBasic, HTTPAuthorizationCredentials, HTTPBearer

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
db = client.python


def basic_authentication(credentials: HTTPBasicCredentials = Depends(HTTPBasic())) -> str:
    correct_username = secrets.compare_digest("user", credentials.username)
    bd_hashed_password = bcrypt.hashpw(b"pass", bcrypt.gensalt())
    correct_password = bcrypt.checkpw(credentials.password.encode('utf-8'), bd_hashed_password)
    print('token:', secrets.token_urlsafe(16))
    print('pass:', bd_hashed_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="usuario o contraseño incorrecta"
        )
    return credentials.username


def bearer_authentication(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> str:
    try:
        paylod = jwt.decode(credentials.credentials, 'secret_key-Y0eT145', algorithms=["HS512", "HS256"])
        username: str = paylod.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="no existe el usuario")
        return username
    except jwt.DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token invalido")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="token expirado")
