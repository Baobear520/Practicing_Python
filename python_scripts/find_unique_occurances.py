from typing import List


# входные данные source = [1, 2, 2, 4, 2, 3, 3]
# написать функцию, которая вернет список чисел, которые встречаются только один раз


def find_single_occurrences(lst: list) -> List[int]:
    count_dict = {}
    # Count occurrences of each number
    for num in lst:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Return only numbers that appear once
    return [num for num, count in count_dict.items() if count == 1]


print(find_single_occurrences([1, 2, 2, 4, 2, 3, 3]))


