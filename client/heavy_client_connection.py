from os import system as sys
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from typing import List



def client(orig_argv: List[str]) -> None:
    print('client started')
    # removing the first and second arguments. (the script name and the path)
    orig_argv.pop(0)
    orig_argv.pop(0)
    
    
    HOST = orig_argv[0]
    PORT = int(orig_argv[1])
    
    if len(orig_argv) > 2:
        key = orig_argv[2]
        data = orig_argv[3]
    
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    
    print(f'connected to server > host:{HOST}, port:{PORT}')
    
    if len(orig_argv) <= 2:
        s.sendall(input('please enter your key: ').encode())
        s.sendall(input('please enter your data: ').encode())
    else:
        s.sendall((key+data).encode())
        # s.sendall(data.encode())
        
    
    response = s.recv(1024).decode()
    print(f'\n\n\nresponse: {response}\n')
    
    s.close()
    



if __name__ == '__main__':
    for i in range(50):
        Thread(target=client, args=(f'python client/client.py 127.0.0.1 8081 e{i}e {i+1}e{i}e{i+2}'.split(),)).start()
        