# Areesha Jamil - Port Scanner
import socket
target = input("Enter IP: ")
print(f"Scanning {target}")
for port in [21,22,80,443]:
    s=socket.socket()
    s.settimeout(1)
    try:
        s.connect((target,port))
        print(f"Port {port}: OPEN")
    except:
        print(f"Port {port}: CLOSED")
    s.close()
