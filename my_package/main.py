def func(x,*args,y):
    print(x)
    
    #if we call func(x,my_list,y)
    print(args) # returns packed tuple ([1,2,3],)
    print(*args) #unpacks the tuple of args and returns [1,2,3]
    
    #if we call func(x,*my_list,y) aka unpack the tuple of args:
    #print(args) returns packed tuple (1,2,3)
    #print(*args) returns a sequence 1 2 3


my_list1 = [1,2,3]
my_list2 = [4,5,6]

func(3,my_list1,y=1)
func(3,*my_list1,y=1)
