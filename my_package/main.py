import sys

def check_allocated_memory(*args:list):
    """Check how much space takes a variable of type list 
    depending on the type of its elements"""
    
    for arg in args:
        print(sys.getsizeof(arg))

    return 

if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    b = ['1','2','3','4','5','6']
    c = ['cat','dog','pig','g','fdfddfd','dffff']
    check_allocated_memory(a,b,c)

