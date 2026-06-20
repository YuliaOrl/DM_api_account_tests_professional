from typing import NamedTuple


class User(NamedTuple):
    login: str
    password: str
    email: str
