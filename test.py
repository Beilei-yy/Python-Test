class person:
    def __init__(self):
        print('嗨，我是人类')
    def __del__(self):
        print('被销毁的人偶')
p = person()
del p  #删除p对象
print("这是倒数第二行代码")
print("这是最后一行代码")

# 面向对象三大要素：封装，多态，继承
# 封装
class Person:
    name = "ding"
#11
