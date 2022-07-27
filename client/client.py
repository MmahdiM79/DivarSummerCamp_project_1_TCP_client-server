import sys
from typing import Tuple
sys.path.insert(1, '/Users/mm.m.mm/Desktop/divar project 1/')

from utils.functions import clear
from sys import orig_argv
from socket import AF_INET, SOCK_STREAM, socket




class TcpClient(object):
    '''
        A simple tcp client.\n
        You can use this class to send and receive data from a over a tcp connection.
    '''
    
    
    
    def __init__(self, host: str='127.0.0.1', port: int=8080, buffer_size: int=1024):
        '''
            :param host: hostname or ip address. (default: 127.0.0.1)
            :param port: port number. (default: 8080)
            :param buffer_size: size of the buffer. (default: 1024)
        '''
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.__sock = socket(AF_INET, SOCK_STREAM)
        
    

    def connect(self) -> None:
        '''
            connect to server.
        '''
        print(f'connected to server > host:{self.host}, port:{self.port}')
        self.__sock.connect((self.host, self.port))
        
        
        
    def disconnect(self) -> None:
        '''
            disconnect from server.
        '''
        self.__sock.close()
        
        
        
    def send(self, data: str) -> int:
        '''
            send data to server.\n
            the data will be encoded to utf-8.
            
            :param data: data to send.
            :return: number of bytes sent.
        '''
        return self.__sock.send(data.encode())
    
    
    
    def recv(self) -> str:
        '''
            receive data from server with buffer_size.\n
            the data will be decoded from utf-8.
            
            :return: data received.
        '''
        return self.__sock.recv(self.buffer_size).decode()
    
    
    
    def __str__(self) -> str:
        return f'host: {self.host}\nport: {self.port}\nbuffer_size: {self.buffer_size}'
    
    def __del__(self) -> None:
        self.__sock.close()
        
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, __o: object) -> bool:
        return self.__str__() == __o.__str__()



def read_args() -> Tuple[str, int]:
    '''
        This function returns the host and port of the server, \n
        from orig_argv
        
        
        :return: (host, port)
    '''
    # removing the first and second arguments. (the script name and the path)
    orig_argv.pop(0)
    orig_argv.pop(0)
    
    host = orig_argv[0]
    port = int(orig_argv[1])
    
    return host, port
    




if __name__ == '__main__':
    clear()

 
    HOST, PORT = read_args()
    client = TcpClient(host=HOST, port=PORT)
    
    
    client.connect()
    
    client.send(data=input('please enter your key: '))
    client.send(data=input('please enter your data: '))
    
    response = client.recv()
    print(f'\n\n\nresponse: {response}\n')
    
    
    client.disconnect()
    