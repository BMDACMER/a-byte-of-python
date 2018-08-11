'''
对象变量（Object variable）由类的每一个独立的对象或实例所拥有。在这种情况下，每个
对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，也不会以任何方式与其
它不同实例中的相同名称的字段产生关联
'''
# coding=UTF-8

class Robot:
    ''' 表示有一个带有名字的机器人 '''
    # 一个类变量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        '''初始化数据'''
        self.name = name
        print(f'(Initializing {self.name})')

        # 当有人被创建时，机器人 将会增加人口数量
        Robot.population += 1

    def die(self):
        '''我挂啦'''
        print(f"{self.name} is being destroyed!")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population}")
    def say_hi(self):
        '''来自机器人的诚挚问候
            没问题，你做得到。
        '''
        print("Greetings, my masters call me {}.".format(self.name))

    # how_many 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个
    # classmethod（类方法） 或是一个 staticmethod（静态方法） ，这取决于我们是否知道我们需不需
    # 要知道我们属于哪个类。由于我们已经引用了一个类变量，因此我们使用 classmethod（类方
    # 法） 。
    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")
print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
