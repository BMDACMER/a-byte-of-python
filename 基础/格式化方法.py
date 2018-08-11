'''
format() 方法的运用
'''

# age = 24
# name = 'G_Hence'
#
# print('{0} was {1} years old when he code the proceduce '.format(name, age))
# print('Why is {0} playing with that python?'.format(name))
#
# print("-------------")
# print(name + ' is ' + str(age) + 'years old')


# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^7}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

#  为了 防止打印过程中出现换行符    可以通过end指定其对应以空白结尾：
print('a',end='')
print('b',end='')
print()
# 转义字符  \\

print('This is the first line\nThis is the second line')

#  原始字符串  在字符串前 增加r或 R 来制定一个 原始（Raw）字符串
print(r"Newlines are indicated\\ by \n")

# i = 5; print(i);j=6

# 如果一行非常长的代码，你可以通过使用反斜杠将其拆分成多个物理行，者将被称作显示行连接
s = 'This is a string.\
    This continues the string.'
print(s)
# 类似的 等同于
i = \
500
print(i)

