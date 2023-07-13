# Nested Function
# def multi(x):
#     def inner_multi(y):
#         return x*y
#     return inner_multi
#
#
# x = multi(10)
# result = x(20)
# print(result)

# We can pass a function as an argument to another function in Python

'''
def saquare(x):
    return x**2


def calculate_squ(func,x):
    return func(x)


result = calculate_squ(saquare,4)
print(result)
'''

# Return a Function as a Value


'''
def invo(name):
    def inner_invo():
        return "hello, " + name
    return inner_invo


name = input('Enter thr name:')
greet = invo(name)
print(greet())
'''


'''
class cricket:
    email = 'email@gmail.com'
    password ='Email@1234'

    def display(self):
        print(self.email,self.password)
    print('Class created Successfully')
c = cricket()
c.display()
'''


'''
class student:
    def __init__(self,name,age):
        self.n = name
        self.a = age

    def student_details(self):
        return "I am {}.I am {} years old.".format(self.n,self.a)

    
name = input('enter the string:')
age = int(input('enter the age'))
s = student(name,age)
k = s.student_details()
print(k)
'''
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age =age


class student(Person):
    def __init__(self, name, age, subject):
        self.subject = subject
        Person.__init__(self,name,age)

    def student_subject(self):
        return "i am {}. I am {} years old. I am studying in {}".format(self.name,self.age,self.subject)


name = input('enter the name:')
age = input('enter the age:')
subject = input('enter the subject:')

person_details= student(name,age,subject)
print(person_details.student_subject())

'''



