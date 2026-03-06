import socket


def getip(addr: str = "1.1.1.1", port: int = 80) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((addr, port))

        return sock.getsockname()[0]


if __name__ == "__main__":
    ips = getip()
    print(getip())
