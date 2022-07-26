import sys
sys.path.insert(1, '/Users/mm.m.mm/Desktop/divar project 1/')

from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM, _RetAddress
from utils.functions import clear
from concurrent.futures import ThreadPoolExecutor
from typing import Callable, List, Tuple





class TcpServer(object):
    '''
        A simple tcp server.\n
        This class handles the tcp connections concurrently.\n
    '''
    
    
    def __init__(self, host: str='127.0.0.1', port: int=8080, buffer_size: int=1024, max_connections: int=16):
        '''
            :param host: hostname or ip address. (default: 127.0.0.1)
            :param port: port number. (default: 8080)
            :param buffer_size: size of the buffer. (default: 1024)
            :param max_connections: maximum number of connections. (default: 16)
        '''
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.__sock = socket(AF_INET, SOCK_STREAM)
        self.__clients = []
        self.__executor = ThreadPoolExecutor(max_workers=max_connections)
        
        
        
    def setup(self) -> None:
        '''
            setup the server.
        '''
        self.__sock.bind((self.host, self.port))
        print(f'server is up > host:{self.host}, port:{self.port}\n\n')
        
        
        
    def down(self) -> None:
        '''
            close the server.
        '''
        print('\n\nserver is shutting down...')
        self.__sock.close()
        self.__executor.shutdown()
        
       
        
    def start(self, func: Callable[[socket], None]) -> None:
        '''
            listen for connections.
            
            :param func: function to call when a connection is established. 
        '''
        self.__sock.listen()
        
        while True:
            try:
                conn, addr = self.__sock.accept()
                print(f'connection from {addr}. [{datetime.now()}]')
                self.__clients.append((conn, addr))
                
                self.__executor.submit(func, conn)


            except KeyboardInterrupt:
                
                exit()
                
                
                
    def clients(self) -> List[Tuple[socket, _RetAddress]]:
        '''
            get the list of clients.
        '''
        return self.__clients
    
    
    def __str__(self) -> str:
        return f'host: {self.host}\nport: {self.port}\nbuffer_size: {self.buffer_size}'






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






if __name__ == '__main__':
    clear()
    
    s = TcpServer()
    s.setup()
    s.start(client_handler)
    
    
    
    