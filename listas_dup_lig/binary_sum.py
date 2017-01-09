def binary_sum(n, n2):
    """n and n2 are non negative binary numbers with arbitrary len. Ex:
     '00010101001010101010101010101010101001010101010101010'
    """
    n = int(n, 2)
    n2 = int(n2, 2)
    return format(n + n2, 'b')


print(binary_sum('111110', '1100'))  # 1001010
