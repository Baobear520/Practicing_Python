def data_source():
    for i in range(10):
        yield i

def filter_even_numbers(data):
    for item in data:
        if item % 2 == 0:
            yield item

def square_numbers(data):
    for item in data:
        yield item * item

# Usage
pipeline = data_source()
pipeline = filter_even_numbers(pipeline)
pipeline = square_numbers(pipeline)

for result in pipeline:
    print(result)