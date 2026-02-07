import random


class Apple:
    total_apple = 0
    total_weight = 0
    
    def __init__(self, weight):
        self.weight = weight
        Apple.total_apple += 1
        Apple.total_weight += self.weight


class ShopOwner():
    def __init__(self):
        self.packages = 0
        self.package_weight = 0
        
    def pack_apple(self, numbers, weight_limit=300):
        package = []
        for i in range(0, numbers):
            aple = Apple(random.uniform(0.2, 0.5))
            if self.package_weight + aple.weight > weight_limit:
                print(f'package {self.packages} total apple {len(package)}')
                print(f'package {self.packages} total weight {self.package_weight}')
                
                self.packages += 1
                self.package_weight = 0
                del package[:]

            self.package_weight += aple.weight
            package.append(aple)

        print(f'package {self.packages} total apple {len(package)}')
        print(f'package {self.packages} total weight {self.package_weight}')

        print(f'Packed {Apple.total_apple} apples with total weight {Apple.total_weight} in {self.packages} packages')

if __name__ == '__main__':
    owner = ShopOwner()
    owner.pack_apple(1000)

