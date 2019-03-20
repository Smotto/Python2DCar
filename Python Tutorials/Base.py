class Base(object):
    def __init__(self, *args, data=None, **kwargs):
        print('data is: ', data)
        print('kwargs are: ', kwargs)


class MyBaseObject(Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MyObject(MyBaseObject):
    def __init__(self, *args, game=None, **kwargs):
        super().__init__(*args, **kwargs)
        print('game is: ', game)

