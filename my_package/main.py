x = 0
def func(x=2):
    print(x)

x = 4
func(3)

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#how to avoid it

def f(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))