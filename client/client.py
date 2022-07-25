import sys
sys.path.insert(1, '/Users/mm.m.mm/Desktop/divar project 1/')

from utils.functions import clear
from sys import orig_argv
from socket import AF_INET, SOCK_STREAM, socket







if __name__ == '__main__':
    clear()
    
    # removing the first and second arguments. (the script name and the path)
    orig_argv.pop(0)
    orig_argv.pop(0)
    
    
    HOST = orig_argv[0]
    PORT = int(orig_argv[1])
    
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    
    print(f'connected to server > host:{HOST}, port:{PORT}')
    
    s.sendall(input('please enter your key: ').encode())
    s.sendall(input('please enter your data: ').encode())
    
    response = s.recv(1024).decode()
    print(f'\n\n\nresponse: {response}\n')
    
    s.close()
    