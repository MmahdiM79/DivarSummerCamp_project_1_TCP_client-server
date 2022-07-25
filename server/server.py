import sys
sys.path.insert(1, '/Users/mm.m.mm/Desktop/divar project 1/')

from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM
from utils.functions import clear
from concurrent.futures import ThreadPoolExecutor







def server_setup(host: str='127.0.0.1', port: int=8080) -> socket:
    '''
        Binds the server to the host and port.
        
        
        :param host: The host to bind to. (default: 127.0.0.1)
        :param port: The port to bind to. (default: 8080)
        :param buffer_size: Size of the buffer. (default: 2**10)
        
        :return: The bound socket.
    '''
    
    print(f'server is up > host:{host}, port:{port}\n\n')
    
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((host, port))
    
    return s





def client_handler(conn: socket, buffer_size: int=2**10) -> None:
    '''
        Handles the client.
        
        
        :param conn: The client socket.
    '''
    
    key = conn.recv(buffer_size).decode()
    print(f'[client {key}] -> key: {key}')
    
    data = conn.recv(buffer_size).decode()
    print(f'[client {key}] -> data: {data}')
    
    data = data.split(key)
    data = map(int, data)
    
    response = sum(data)
    conn.send(str(response).encode())
    
    print(f'[client {key}] <- response: {response}')
    print(f'[client {key}] <- disconnected.\n\n')
    
    
    conn.close()





def server_listen(s: socket, n: int=16) -> None:
    '''
        Listens for connections on the given socket.\n
        If a connection is made, the server will accept it and handle it.\n
        See server.client_handler() for more information.
        
        
        
        :param s: The socket to listen on.
        :param n: The number of connections to accept. (default: 100)
    '''
    
    executor = ThreadPoolExecutor(max_workers=n)
    
    
    s.listen()
    
    while True:
        try:
            conn, addr = s.accept()
            print(f'connection from {addr}. [{datetime.now()}]')
            
            executor.submit(client_handler, conn)


            
        except KeyboardInterrupt:
            print('\n\nserver is shutting down...')
            s.close()
            executor.shutdown()
            exit()

    
    
    



if __name__ == '__main__':
    clear()
    
    s = server_setup()
    server_listen(s)
    
    
    
    