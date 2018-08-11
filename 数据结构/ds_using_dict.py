'''
换言之，我们将键值（Keys）（即姓名）与值（Values）（即地
址等详细信息）联立到一起

另外要注意的是你只能使用不可变的对象（如字符串）作为字典的键值，但是你可以使用可
变或不可变的对象作为字典中的值。
'''
# “ab”是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'Swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值---值配对
del ab['Spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
# print(f'\nThere are {len(ab)} contacts in the address-book\n')

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

print("-----------------------\n")
# 再次添加一对键值--值配对
ab['guohao'] = '1163753605@qq.com'
for name, address in ab.items():
    print(f'Contact {name} at {address}')