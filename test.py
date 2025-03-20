class person:
    def __init__(self):
        print('嗨，我是人类')
    def __del__(self):
        print('被销毁的人偶')
p = person()
