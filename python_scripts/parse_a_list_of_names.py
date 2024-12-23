from functools import  reduce


NAMES = ['brian okken', 'michael kennedy', 'trey hunner',
                       'matt harrison', 'julian sequeira', 'dan bader',
                       'michael kennedy', 'brian okken', 'dan bader']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    return list(set(map(lambda x: x.title(), names)))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda name: name.split()[-1])


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    return min((name.split()[0] for name in names), key=len)



print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))