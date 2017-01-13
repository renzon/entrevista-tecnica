def dedup(lst):
    """Remove duplicates from lst

    :param lst: a list
    :return: new list without duplicated elements

    linear for time and space
    """
    result = []
    repeated = set()

    for ele in lst:
        if ele not in repeated:
            result.append(ele)
            repeated.add(ele)
    return result


print(dedup(['banana', 'banana', 'banana', 'abacaxi', 'caqui']))
