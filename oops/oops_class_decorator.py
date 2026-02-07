def object_counter(class_):
    class_.__get_attr_org = class_.__getattribute__

    def get_attr_wrapper(self, name):
        if name == "VIN":
            print('VIN is being accessed')
            return class_.__get_attr_org(self, name)

    class_.__getattribute__ = get_attr_wrapper
    return class_

@object_counter
class Car:
    def __init__(self, VIN):
        self.mileage = 0
        self.VIN = VIN

car = Car('ABC123')
print('The mileage is', car.mileage)
print('The VIN is', car.VIN)