from passlib.context import CryptContext

pass_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hash(password: str):
    return pass_cxt.hash(password)


def verify(plain_password: str, password: str) -> bool:
    return pass_cxt.verify(plain_password, password)
