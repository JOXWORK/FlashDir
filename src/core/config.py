from socket import AF_INET, SOCK_STREAM
from dataclasses import dataclass
from getip import getip


@dataclass
class Settings:
    HOST = getip()
    PORT = 65000

    SOCK_FAMILY = AF_INET
    SOCK_TYPE = SOCK_STREAM


settings = Settings()
