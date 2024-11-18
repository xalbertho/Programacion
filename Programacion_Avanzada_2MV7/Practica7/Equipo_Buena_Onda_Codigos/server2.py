import socket
import threading

class Cliente:
    def __init__(self, conn, addr):
        self.name = ""
        self.conn = conn
        self.addr = addr

def client_thread(conn, addr):
    conn.send(bytes("Bienvenido, por favor envía tu nombre de usuario con '<name>tu_nombre'.\n", 'utf-8'))
    while True:
        try:
            message = conn.recv(BUFFER_SIZE)
            if message:
                msg = message.decode('utf-8')
                print(f"<{addr[0]}> {msg}")

                if msg.startswith('<search>'):
                    search_name = msg.removeprefix('<search>').strip()
                    result = search_user(search_name)
                    conn.send(bytes(f"search_result:{result}\n", 'utf-8'))
                elif msg.startswith('<name>'):
                    setName(conn, msg.removeprefix('<name>'))
                elif msg.startswith('<private>'):
                    # El formato esperado es '<private>:recipient_name:actual_message'
                    _, recipient_name, actual_message = msg.split(':', 2)
                    send_private_message(recipient_name, actual_message, conn)
                else:
                    name = getName(conn)
                    if name:  # Asegurarse de que el nombre está establecido antes de retransmitir
                        broadcast(f"<{name}> {msg}\n", conn)
            else:
                remove(conn)
                break
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
            remove(conn)
            break

def send_private_message(recipient_name, message, sender_conn):
    # La búsqueda debe ser insensible a mayúsculas/minúsculas y trim espacios
    recipient_name = recipient_name.strip().lower()
    recipient = next((client for client in list_of_clients if client.name.lower() == recipient_name), None)
    if recipient:
        try:
            recipient.conn.send(bytes(f"De {getName(sender_conn)}: {message}", 'utf-8'))
            recipient.conn.send(bytes(f"notify:{getName(sender_conn)}", 'utf-8'))
        except Exception as e:
            print(f"Error sending private message to {recipient_name}: {e}")
            sender_conn.send(bytes(f"Error sending message to {recipient_name}.", 'utf-8'))
    else:
        sender_conn.send(bytes(f"No such user: {recipient_name}", 'utf-8'))


def search_user(name):
    found = [client.name for client in list_of_clients if client.name.lower().startswith(name.lower())]
    return ','.join(found) if found else 'No results'

def setName(connection, name):
    for client in list_of_clients:
        if client.conn == connection:
            client.name = name.strip().lower()  # Asegúrate de manejar correctamente los nombres
            break

def getName(connection):
    for client in list_of_clients:
        if client.conn == connection:
            return client.name
    return ""
def broadcast(message, sender_conn):
    for client in list_of_clients:
        if client.conn != sender_conn:
            try:
                client.conn.send(bytes(message, 'utf-8'))
            except:
                remove(client)

def remove(connection):
    global list_of_clients
    list_of_clients = [client for client in list_of_clients if client.conn != connection]
    connection.close()

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    BUFFER_SIZE = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(100)
    list_of_clients = []
    print(f"Escuchando conexiones en: {(host, port)}")

    try:
        while True:
            conn, addr = server.accept()
            nuevo_cliente = Cliente(conn, addr)
            list_of_clients.append(nuevo_cliente)
            print(f"Cliente conectado desde {addr}")
            threading.Thread(target=client_thread, args=(conn, addr)).start()
    except KeyboardInterrupt:
        print("Servidor interrumpido por el usuario")
    finally:
        for client in list_of_clients:
            client.conn.close()
        server.close()
        print("Conexión terminada.")
