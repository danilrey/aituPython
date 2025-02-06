import random

class func_in_random_order:
    def __init__(self):
        self.funcs = []

    def add_func(self, func):
        self.funcs.append(func)
        return func

    def __iter__(self):
        return self.generate_funcs()

    def generate_funcs(self):
        rand = self.funcs[:]
        random.shuffle(rand)
        for func in rand:
            yield func

result = func_in_random_order()

def register(function):
    return result.add_func(function)

# Using the custom register function
@register
def func1():
    print("Function 1 executed")

@register
def func2():
    print("Function 2 executed")

@register
def func3():
    print("Function 3 executed")

for func in result:
    func()