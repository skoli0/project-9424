def _print(n):
    if n <= 0:
        return n
    print(n)

    return _print(n-1)

def add(n):
    if n <= 0:
        return 0

    return n + add(n-1)

def _pow(a, b):
    if b == 0:
        return 1

    return a * _pow(a, b-1)
    # if b % 2 == 0: return _pow(a*a, b/2)
    # else: return a * _pow(a, b-1)

def path(row, col):
    if row == 1 or col == 1: return 1

    return path(row, col-1) + path(row-1, col)

def permute(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

_print(10)
print(add(10))
print(_pow(2, 30))
print(path(4, 4))
print('====String permutation====')
a = list('abc')
permute(a, 0, len(a)-1)
