# 集合

bri = set(['brazil', 'rusia', 'india'])
print('india' in bri)

bric = bri.copy()
bric.add('China')
print(bric.issuperset(bri))   # 父类
print(bric.issubset(bri))     # 子类
print("==============================")
bri.remove('rusia')
print(bri)
print(bric)
print(bri & bric)