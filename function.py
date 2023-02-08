def sayhello():
    print('hello')
    print('hello')

def square(x):
    print(f'Квадрат числа {x} = {x**2}')

def multiply(x,y):
    print(f'{x} * {y} = {x*y}')

def even(a):
    print(a,'четное' if a % 2 == 0 else 'не четное')

def factorial(x):
    pr = 1
    for i in range(2,x+1):
        pr = pr * i
    print(f'факториал числа {x} = {pr}')

sayhello()
square(2)
multiply(3,4)
for i in range(30,34):
    even(i)
print()
factorial(9)