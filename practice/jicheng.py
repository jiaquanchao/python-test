# coding:utf8

class animal(object):
    def move(self):
        print('can move via different mode')

    def eat(self):
        print('living need food')

    def outlook(self):
        print('like something')
class ufo(object):
    def eat(self):
        print('这也行？')

    def outlook(self):
        print('like a dish')

class dog(animal):
    def move(self):
        print('dog run! run fast')

    def eat(self):
        print('dog eats vagetable and meat')

    def outlook(self):
        print('dog')

class bird(animal):
    def move(self):
        print('bird fly')

    def eat(self):
        print('bird eats seed')

    def outlook(self):
        print('bird')

def taste(animal):
    animal.outlook()

if __name__ == '__main__':

    taste(dog())
    taste(ufo())

    animal = animal()
    animal.eat()
