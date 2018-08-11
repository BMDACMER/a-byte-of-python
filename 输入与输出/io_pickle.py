import pickle

'''
Python 提供了一个叫作 Pickle 的标准模块，通过它你可以将任何纯 Python 对象存储到一
个文件中，并在稍后将其取回。这叫作持久地（Persistently）存储对象。
'''
# The name of the file where we will store the object
shoplistfile = 'shoplist.txt'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplistfile, f)
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
