PASSWORD  = '1234'

def password_required(func):
    def wrapper():
        password = input('cual es tu contraseña')
        
        if password == PASSWORD:
            return func()
        else:
            print('la contraseña no es correcta')
    return wrapper


@password_required
def needs_password():
    print('la contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func (*args, **kwargs)

        return result.upper()
    return wrapper



@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)




if __name__ == '__main__':
    # needs_password()
   
   print (say_my_name('mynor'))
