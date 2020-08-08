# Insertion Sort
# Function for Insertion Sort


def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        value = a[i]
        j = i
        while (j > 0 and a[j-1] > value):
            a[j] = a[j-1]
            j -= 1

        a[j] = value

if __name__ == '__main__':

    a = [55, 22, 33, 66, 11, 77, 0]
    insertion_sort(a)
    print(a)
