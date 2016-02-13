
# Factory patter is a creational design pattern used to get object of different type at run time

# Pet Store using Factory Design Pattern to sell Dogs and Cats
class Dog:
    def __init__(self,name):
        self._name = name

    def speak(self):
        print "Bark..."

class Cat:
    def __init__(self,name):
        self._name = name

    def speak(self):
        print "Meow!!!"


def get_pet(pet ="dog"):

    pets = dict(dog = Dog("Hope"), cat = Cat("Peace"))
    return pets[pet]

def main():
    dog = get_pet("dog")
    dog.speak()

    cat = get_pet("cat")
    cat.speak()

if __name__ == '__main__':
    main()