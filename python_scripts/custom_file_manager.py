
class FileManager:
    def __init__(self, file_path, mode='r'):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, 'r')
            return self.file
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

my_file = FileManager('file.txt')

with my_file as file:
    if file:
        print(file.read())