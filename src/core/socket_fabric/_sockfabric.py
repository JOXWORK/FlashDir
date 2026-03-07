import socket
from functools import wraps
from core.config import settings


def sockfab(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with socket.socket(settings.SOCK_FAMILY, settings.SOCK_TYPE) as sock:
            return func(sock, *args, **kwargs)

    return wrapper
