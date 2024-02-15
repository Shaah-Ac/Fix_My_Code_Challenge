#!/usr/bin/python3
"""
 User Model
"""
import hashlib
import uuid


class User:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        if pwd is None or not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        if pwd is None or not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Test User")

    user_1 = User()
    assert user_1.id is not None, "New User should have an id"

    user_2 = User()
    assert user_1.id != user_2.id, "User.id should be unique"

    u_pwd = "myPassword"
    user_1.password = u_pwd
    assert user_1.password != u_pwd, "User.password should be hashed"

    assert user_2.password is None, "User.password should be None by default"

    user_2.password = None
    assert user_2.password is None, "User.password should be None if set to None"

    user_2.password = 89  # Attempt to set password to an integer
    assert user_2.password is None, "User.password should be None if set to an integer"

    assert user_1.is_valid_password(u_pwd), "is_valid_password should return True if it's the right password"
    assert not user_1.is_valid_password("Fakepwd"), "is_valid_password should return False if it's not the right password"
    assert not user_1.is_valid_password(None), "is_valid_password should return False if compare with None"
    assert not user_1.is_valid_password(89), "is_valid_password should return False if compare with an integer"
    assert not user_2.is_valid_password("No pwd"), "is_valid_password should return False if no password set before"

    print("All tests passed successfully.")
