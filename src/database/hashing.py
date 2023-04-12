from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    """Class for hashing passwords."""

    def get_bcrypt_hashed_password(password: str) -> str:
        """Creates a brcypt hashed password."""
        hashed_password = pwd_cxt.hash(password)
        return hashed_password

    def get_scrypt_hashed_password(password: str) -> str:
        """Creates a scrypt hashed password."""
        pwd_cxt = CryptContext(schemes=["scrypt"], deprecated="auto")
        hashed_password = pwd_cxt.hash(password)
        return hashed_password

    def verify(hashed_password: str, plain_password: str) -> bool:
        """Verifies if two passwords are equal."""
        return pwd_cxt.verify(plain_password, hashed_password)
