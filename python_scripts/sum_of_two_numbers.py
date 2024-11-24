
def find_two_nums(my_list: list[int], total):

    checked_elements = set()
    for element in my_list:
        remainder = total - element
        if remainder in checked_elements and remainder != 0:
            print(remainder, element)

        checked_elements.add(element)


find_two_nums([3,7,2,5,4],7)



