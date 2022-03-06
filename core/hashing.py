from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"],deprecated = "auto")


class Hasher():
    @staticmethod
    def verify_password(plain,hashed):
        return pwd_context.verify(plain,hashed)

    @staticmethod
    def get_password_hash(plain):
        return pwd_context.hash(plain)