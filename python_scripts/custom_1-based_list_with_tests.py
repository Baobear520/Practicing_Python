

class CustomList(list):
    def __getitem__(self, item):

        if item == 0:
            raise IndexError("Indices cannot be 0")
        elif item > 0:
            item -= 1
        return super().__getitem__(item)


class TestCustomList:
    def __init__(self, custom_list, lst):
        self._custom_list = custom_list
        self._lst = lst

    def test_for_equality(self):
        assert self._lst[0] == self._custom_list[1]

    def test_for_zero(self):
        try:
            self._custom_list[0]
            assert False,  "Expected IndexError but no exception was raised"
        except IndexError as e:
            assert str(e) == "Indices cannot be 0"

    def test_for_negative_indices(self):
        assert self._custom_list[-1] == self._lst[-1]


def run_tests():
    my_list = ['hello', 'hi', 'bye']
    obj = CustomList(my_list)

    test = TestCustomList(obj, my_list)

    # Запускаем тесты по одному и выводим результат
    for name in [method for method in dir(test) if method.startswith('test_')]:
        try:
            getattr(test, name)()
            print(f"✅ {name} passed")
        except AssertionError as e:
            print(f"❌ {name} failed: {e}")

if __name__ == "__main__":
    run_tests()



