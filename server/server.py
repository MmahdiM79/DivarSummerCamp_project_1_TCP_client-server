from socket import socket, AF_INET, SOCK_STREAM
from os import argv
from utils.functions import clear





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

    



if __name__ == '__main__':
    clear()
        
    