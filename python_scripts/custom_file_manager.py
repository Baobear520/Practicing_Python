
class CustomFileManager:
    def __init__(self, path_to_file, mode='r', encoding='utf-8'):
        self.path_to_file = path_to_file
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):

        self.file = open(self.path_to_file, self.mode, encoding=self.encoding)
        return self.file


    def __exit__(self, exc_class, exc_value, traceback):

        self.file.close()
        if exc_class is None:
            print("File closed successfully.")
        else:
            print(f"{type(exc_class).__name__} occurred: {exc_value}, {traceback}")


path_to_file = '/Users/aldmikon/Desktop/keyword.txt'
my_file = CustomFileManager(path_to_file)


try:
    with my_file as f:
        print(f.read())
except FileNotFoundError:
    print(f"File {path_to_file} not found.")
except Exception as e:
    print(f"{type(e).__name__} occurred: {e} ")


from contextlib import contextmanager

@contextmanager
def file_manager(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open('/Users/aldmikon/Desktop/phrases.txt') as file:
    print(file.read())