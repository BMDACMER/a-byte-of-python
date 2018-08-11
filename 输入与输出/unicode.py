'''
我们需要将我们的 Unicode 字符串转换至一个能够被发送和接收的格式，这个格式叫作“UTF-8”。我们可以在
这一格式下进行读取与写入，只需使用一个简单的关键字参数到我们的标准 open 函数中
'''

# encoding=utf-8
import io

f = io.open("abc.txt","wt",encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)
