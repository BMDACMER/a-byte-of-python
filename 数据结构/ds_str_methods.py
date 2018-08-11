# 这是一个字符串对象
'''
find 方法用于定位字符串中给定的子字符串的位置。如果找不到相应的子字符串， find
会返回 -1。
str 类同样还拥有一个简洁的方法用以 联结（Join） 序列中的项目，其中字符串
将会作为每一项目之间的分隔符，并以此生成并返回一串更大的字符串。
'''
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a'  in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(mylist)
print(delimiter.join(mylist))
