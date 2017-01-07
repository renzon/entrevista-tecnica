def hanoi(n, orig='A', aux='B', dest='C'):
    """Recursive Solution to Hanoi Tower
    t(n) = 1 + 2(t(n-1))
    t(n) = 1 + 2 + 4(t(n-2))
    t(n) = 1 + 2 + 4 + 8(t(n-3))
    t(n) = 1 + 2 + 4 + 8 + 16(t(n-4))
    t(n) = 1 + 2 + 4 + 8 + 16 ... 2**n
    2(t(n)) = 2 + 4 + 8 + 16 + 32 ... 2**(n+1)

    t(n)=2**(n+1)-1 => O(2**n)

    m(n) = 1 + m(n-1) => O(n)
    """
    stack = [(False, n, orig, aux, dest)]

    while stack:
        print_flag, n, orig, aux, dest = stack.pop()
        if n < 1:
            continue
        if not print_flag:
            stack.append((True, n, orig, aux, dest))
            stack.append((False, n - 1, orig, dest, aux))
        else:
            print('{} -> {} : {}'.format(orig, dest, n))
            stack.append((False, n - 1, aux, orig, dest))


for i in range(1, 4):
    print('####### Hanoi %s' % i)
    hanoi(i)
