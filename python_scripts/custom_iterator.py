

class MyIter:
    def __init__(self,maximum):
        self.maximum = maximum
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.maximum:
            self.current += 1
            return self.current
        raise StopIteration


a = MyIter(3)
for i in a:
    print(i)

