class Base:
    def __init__(self, *args, **kwargs):
        print('Base initializer')

    def f(self):
        print('Base.f()')


class Sub(Base):
    def __init__(self, *args, **kwargs):
        super().__init__()
        print('Sub initialiazer')

    def f(self):
        print('Sub.f()')