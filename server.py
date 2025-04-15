import socket

# Server Congfiguration
# This server listens for incoming connections and echoes back any data received.
# It handles socket errors and unexpected exceptions.

HOST = '127.0.0.1' #Localhost
PORT = 65432       # Port to listen on

def start_server():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to host and port
        s.bind((HOST, PORT))


        s.listen()
        print(f"Server is listening on {HOST}:{PORT}")


        conn, addr = s.accept()
        print(f"Connected by {addr}")


        with conn:
            while True:
                data = conn.recv(1024)
                if not data or data.decode().lower() == "exit":
                    print("Client disconnected.")
                    break
                print(f"Received from client: {data.decode()}")
                conn.sendall(data)

    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:

        s.close()
        print("Server socket closed.")

if __name__ == "__main__":
    start_server()