'''
你应该如何确保文件对象被正确关闭，无论是否会发
生异常？这可以通过 finally 块来完成。
'''
# 另外要注意到我们在 print 之后使用了 sys.stout.flush() ，以便它能被立即打印到屏幕
# 上。

import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们尝试用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+d now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem..txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
