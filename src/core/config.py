from dataclasses import dataclass
from getip import getip


@dataclass
class Settings:
    HOST = getip()
    PORT = 65000


settings = Settings()
