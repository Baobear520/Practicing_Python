
def remove_duplicates_and_sort(my_array:list):
    """Remove all the duplicates and sort"""

    my_set = set(my_array)
    print(sorted(my_set))

if __name__ == "__main__":
    my_array = [3,2,6,1,7,4,2,6,9,3,5,5,7]
    remove_duplicates_and_sort(my_array)


