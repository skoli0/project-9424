# Time: 
#   Best: O(n)
#   Average: O(n^2)    
#   Worst-O(n^2)
#   
# Space: O(1)

def bubble_sort(a):
    n = len(a)

    '''
    for i in range(n-1, -1, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    '''

    for i in range(n):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

def bubble_sort_improved(a):
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True

        if not swapped: break
    

a = [5, 2, 3, 6, 1, 7, 0]

print(a)
#bubble_sort(a)
bubble_sort_improved(a)
print(a)
