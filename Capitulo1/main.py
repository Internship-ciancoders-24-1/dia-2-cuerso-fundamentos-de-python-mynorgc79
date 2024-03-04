
clients = 'pablo,mynor,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clientes += client_name
        _add_comma()
    else:
        print('the client already in the client\s list')

    
    

def _add_comma():
    global clients

    clients += ','


def _print_welcome():
    print('WELCOME TO PLAZI VENTAS')
    print('*'*50)
    print('what do you like to do today?')
    print('[C] create client')
    print('[D] delete client')
    


def list_clients():
    global clients
    print(clients)

if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('what is the cliente name?')
        create_client(client_name)
        list_clients()

    elif command == 'D':
        pass
    else:
        print('Invalid Command')

    