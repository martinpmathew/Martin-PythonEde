class SimpleDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before calling the function.")
        result = self.func(*args, **kwargs)
        print("After calling the function.")
        return result


@SimpleDecorator
def combiner(*args, **kwargs):
    print("Hello from the decorated function; received arguments:", args, kwargs)


combiner("a", "b", exec="yes")
