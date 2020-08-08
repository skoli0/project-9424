
def shell_sort(a):
    n = len(a)
    interval = n//2
    while interval > 0:

        for i in range(interval, n):
            key = a[i]
            j = i
            while j >= interval and a[j-interval] > key:
                a[j] = a[j-interval]
                j -= interval
            a[j] = key

        interval //= 2


a = [55, 22, 33, 66, 11, 77, 0]
print(a)
shell_sort(a)
print(a)
