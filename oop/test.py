

class info:
    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print('my name is %s and my age %i' % (self.name, self.age))


r = info("reza", 12)

# r.get_info()


class Computer:
    counter = 0

    def __init__(self, hard, ram, cpu):
        self.hard = hard
        self.ram = ram
        self.cpu = cpu

    def get_info(self):
        print('computer: hard is %s | ram is %i | cpu is %i' %
              (self.hard, self.ram, self.cpu))

    def value(self):
        return self.hard + self.ram + self.cpu


class Laptop(Computer):
    def value(self):
        return self.hard + self.ram + self.cpu + 2


com = Computer(10, 5, 10)
laptop = Laptop(5, 6, 9)


print(com.value())
print(laptop.value())
