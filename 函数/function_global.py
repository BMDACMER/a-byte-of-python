'''
global 语句用以声明 x 是一个全局变量——因此，当我们在函数中为 x 进行赋值时，这
一改动将影响到我们在主代码块中使用的 x 的值。
你可以在同一句 global 语句中指定不止一个的全局变量，例如 global x, y, z 。
'''

x = 50

def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
