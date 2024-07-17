# for immutable data types both operations create a new object
a = 'fog'
b = a
print(f'"a": {a}, ID "a": {id(a)}, "b": {b}, ID "b": {id(b)}')
a += 's'
print(f'"a": {a}, ID "a": {id(a)}, "b": {b}, ID "b": {id(b)}')

a = 'fog'
b = a
print(f'"a": {a}, ID "a": {id(a)}, "b": {b}, ID "b": {id(b)}')
a = a + 's'
print(f'"a": {a}, ID "a": {id(a)}, "b": {b}, ID "b": {id(b)}')










