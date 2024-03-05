class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def say_hello(self):
        print('my name is {} adn I am {} years oold'.format(self.name, self.age))


if __name__ == '__main__':
    person = Person('Mynor', 24)

    print('Age:{}'.format(person.age))
    person.say_hello()

    
