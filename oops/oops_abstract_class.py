import abc

class BluePrint(abc.ABC):
    @abc.abstractmethod
    def hello(self):
        pass

class GreenField(BluePrint):
    def hello(self):
        print('Welcome to Green Field!')


class RedField(BluePrint):
    def yellow(self):
        pass


gf = GreenField()
gf.hello()

# TypeError: Can't instantiate abstract 
# class RedField with abstract methods hello
rf = RedField()

# TypeError: Can't instantiate abstract 
# class BluePrint with abstract methods hello
bp = BluePrint() 