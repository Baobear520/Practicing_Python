import copy

a = 'dog'
b = copy.copy(a)

print(id(a),id(b))

a += 's'
print(id(a),id(b))

b = copy.deepcopy(a)
print(id(a),id(b))