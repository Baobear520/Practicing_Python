
def create_dictionaries_from_word(word):
    """
    Create two dictionaries from a word:
    - dict_1: Mapping of characters to their indices
    - dict_2: Subset of dict_1 where values are zero
    """
    dict_1 = {char: idx for idx, char in enumerate(word)}
    dict_2 = {char: idx for char, idx in dict_1.items() if idx == 0}
    return dict_1, dict_2

def play_with_items(dict_1, dict_2):
    """
    Perform various dictionary operations.
    """
    dict_2['c'] = 1
    dict_1.update(a=5)
    dict_1.pop('t', None)  # Use pop with default to avoid KeyError if 't' doesn't exist
    if dict_1:
        dict_1.popitem()
    dict_2.update(b=10)
    dict_2.setdefault('m', 7)
    return dict_1, dict_2

def check_in_place_modification(dict_2):
    """
    Check in-place modification of dictionary items.
    """
    # If 'm' is a mutable object
    dict_2['m'] = [3]
    print('Mutable before:', id(dict_2['m']))
    dict_2['m'] += [2]
    print('Mutable after:', id(dict_2['m']))
    
    # If 'm' is immutable
    dict_2['m'] = 3
    print('Immutable before:', id(dict_2['m']))
    dict_2['m'] += 2
    print('Immutable after:', id(dict_2['m']))

def check_reassignment(dict_2):
    """
    Check reassignment of dictionary items.
    """
    dict_2['m'] = 3
    print('Before reassignment:', id(dict_2['m']))
    try:
        dict_2['m'] = dict_2['m'] + [2]  # This will raise a TypeError
    except TypeError:
        print('Caught TypeError for immutable and list concatenation.')
    print('After reassignment:', id(dict_2['m']))

def merge_dictionaries(*dicts):
    """
    Merge multiple dictionaries into one.
    """
    merged_dict = {k: v for d in dicts for k, v in d.items()}
    print('Merged dictionary:', merged_dict)
    return merged_dict

if __name__ == "__main__":
    dict_1, dict_2 = create_dictionaries_from_word('cat')
    dict_1, dict_2 = play_with_items(dict_1, dict_2)
    
    # Uncomment to check in-place modification and reassignment
    # check_in_place_modification(dict_2)
    # check_reassignment(dict_2)
    
    merged_dict = merge_dictionaries(dict_1, dict_2)











