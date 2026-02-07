class Example:
    __internal_counter = 0

    def __init__(self, value):
        self.__internal = value
        Example.__internal_counter += 1
    
    @classmethod
    def get_internal(cls):
        return '# of instances created: {}'.format(cls.__internal_counter)

print(Example.get_internal())

example = Example(10)
print(example.get_internal())

print(Example.get_internal())

example2 = Example(99)
print(example2.get_internal())

print(Example.get_internal())


class Car:
    def __init__(self, vin):
        print('Ordinary __init__ was called for', vin)
        self.vin = vin
        self.brand = ''

    @classmethod
    def including_brand(cls, vin, brand):
        print('Class method was called')
        
        # Created a new instance of Car using
        #  the class method and set the brand attribute
        _car = cls(vin)
        _car.brand = brand
        return _car

car1 = Car('ABCD1234')
car2 = Car.including_brand('DEF567', 'NewBrand')

print(car1.vin, car1.brand)
print(car2.vin, car2.brand)

