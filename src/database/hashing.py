from passlib.context import CryptContext


class Hash:
    """Class for hashing passwords."""

    def get_bcrypt_hashed_password(password: str) -> str:
        """Creates a brcypt hashed password."""
        pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = pwd_cxt.hash(password)
        return hashed_password

    def get_scrypt_hashed_password(password: str) -> str:
        """Creates a scrypt hashed password."""
        pwd_cxt = CryptContext(schemes=["scrypt"], deprecated="auto")
        hashed_password = pwd_cxt.hash(password)
        return hashed_password
