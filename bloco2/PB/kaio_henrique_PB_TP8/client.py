import socket, sys

HOST = "127.0.0.1"
PORT = 9999
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_staggered_scheeduling():
    client.connect((HOST, PORT))
    client.send("1".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listing scheduled functions on the server: ", HOST, PORT)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_network_interfaces():
    client.connect((HOST, PORT))
    client.send("2".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listing available network interfaces on the server: " , HOST, PORT)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def menu():
    print("""
    1 - Run scheduled functions
    2 - List available network interfaces
    3 - Exit
    """)

def main():
    menu()
    while True:
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                server_staggered_scheeduling()
            elif choice == 2:
                get_network_interfaces()
            elif choice == 3:
                sys.exit()
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

if __name__ == "__main__":
    sys.exit(main())
