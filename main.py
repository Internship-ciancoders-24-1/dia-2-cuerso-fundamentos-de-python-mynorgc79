
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
    print('[U] update client')
    print('[S] search client')
    print('[L] list clients')


def _get_client_name():
    client_name = None

    while not client_name:
        client_input = input('What is the client name?')
    return client_name
    


def list_clients():
    global clients
    print(clients)


def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is not in clientss list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else: print('Clients is not in clients list')


def search_client(client_name):
    clients_list = clients.split(',')  #utiliza la funcion split que divide el string en comas

    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
        




if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        delete_client (client_name)
        list_clients()
        
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input ('What is the update client name')
        update_client(client_name, update_client_name)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        
        if found:
            print('The client is in the clients list')
        else:
            print('The client: {} is not in our client list'.format(client_name))

    else:
        print('Invalid Command')

    