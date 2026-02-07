class WhareHouseDecorator:
    def __init__(self, material):
        self.material = material

    def __call__(self, our_function):
        def internal_wrapper(*args, **kwargs):
            print('<strong>*</strong> Wrapping items from {} with {}'.format(our_function.__name__, self.material))
            our_function(*args, **kwargs)
            print()
        return internal_wrapper


@WhareHouseDecorator('bubble foil')
def pack_books(*args):
    print("We'll pack books:", args)


@WhareHouseDecorator('foil')
def pack_toys(*args):
    print("We'll pack toys:", args)


@WhareHouseDecorator('cardboard')
def pack_fruits(*args):
    print("We'll pack fruits:", args)


pack_books('Alice in Wonderland', 'Winnie the Pooh')
pack_toys('doll', 'car')
pack_fruits('plum', 'pear')
