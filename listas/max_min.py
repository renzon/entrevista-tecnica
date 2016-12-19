from random import shuffle


def max_min(lst):
    """
    Calculate the maximum and minimum of a list lst
    :param lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:  # lst = [1, ... 99]
        raise ValueError('Empty List')
    max_value = min_value = lst[0]

    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value  # O(n)


print(max_min([1]))  # 1,1
print(max_min([1, 2]))  # 2,1
random_list = list(range(100))
shuffle(random_list)
print(random_list)
print(max_min(random_list))  # 99,0
print(max_min([]))
