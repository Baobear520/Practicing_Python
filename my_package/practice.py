class Foo(object):
    obj = 0

    def __new__(cls, *dt, **mp):
        print(cls, end=' ')
        return object.__new__(cls, *dt, **mp).obj

    def __init__(self):
        self.obj += 2
        print(self, end=' ')

    def __str__(self, x):
        return obj

o = Foo()
#print(o, end=' ')