def message(str):
    def inside_message():
        return "Welcome to "
    return inside_message() + str


def mes_value(name):
    return name


print(message(mes_value('my new home')))


def message(fun):
    def inside_message(name):
        return "Welcome to " + fun(name)
    return inside_message

@ message
def mes_value(name):
    return name


print(mes_value('my new home'))


def test(text):
    return text.lower()
print(test('HELLo'))

x =test
print(x('HEllo WORLd'))

# can be passed as arguments to other functions
def add(x,y):
    return x+y


def sub(x,y):
    return x-y


def maths_opers(func):
    z = func(10,20)
    print(z)


maths_opers(add)
maths_opers(sub)

# Functions can return another function

def adder(x):
    def add(y):
        return x+y
    return add


z = adder(10)
print(z(50))