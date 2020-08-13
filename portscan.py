import socket

portas = [21, 23, 80, 443, 8080]

for c in portas:
    cliente = socket.socket((socket.AF_INET, socket.SOCK_STREAM))
    cliente.settimeout(0.1)
    codigo = cliente.connect_ex(('site.com', c))
    if codigo == 0:
        print(c, "OPEN")