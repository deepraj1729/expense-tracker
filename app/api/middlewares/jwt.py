from fastapi.security import OAuth2PasswordBearer
import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def decodeJWT(token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return decoded

def generateRefreshToken():
    pass