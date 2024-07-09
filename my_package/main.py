
def remove_duplicates_and_sort(my_array:list):
    """Remove all the duplicates and sort"""

    my_set = set(my_array)
    print(sorted(my_set))


def check_set_of_ints(my_set_of_ints:set):
    print(my_set_of_ints)

def check_set_of_strs(my_set_of_strs:set):
    print(my_set_of_strs)

if __name__ == "__main__":
    my_set_of_ints = {3,2,1,2,3}
    check_set_of_ints(my_set_of_ints)

    my_set_of_strs = {'b','d','a','c','b','a'}
    check_set_of_strs(my_set_of_strs)
    
    my_array = [3,2,1,2,3]
    remove_duplicates_and_sort(my_array)



