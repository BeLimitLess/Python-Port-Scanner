import socket


def print_banner():
    banner = """
  _               __                       
 |_) _  ._ _|_   (_   _  _. ._  ._   _  ._ 
 |  (_) |   |_   __) (_ (_| | | | | (/_ |  
                                            
                                               
"""
    print(banner)


def get_accessible_ports(address, min_port, max_port):
    found_ports = []

    for port in range(min_port, max_port + 1):
        s = socket.socket()
        if s.connect_ex((address, port)) == 0:
            found_ports.append(port)
        s.close()
    return found_ports


print_banner()

address = input("Enter the IP Address: ")
min_port = int(input("Start port no: "))
max_port = int(input("End port no: "))
print("Starting Scan")

ports = get_accessible_ports(address, min_port, max_port)


print("Open Ports: ")
for p in ports:
    print(p)
