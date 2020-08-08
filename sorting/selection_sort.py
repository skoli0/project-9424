# Time: 
#   Best: O(n^2)
#   Average: O(n^2)    
#   Worst-O(n^2)
#   
# Space: O(1)

def selection_sort(a):
    n = len(a)

    for i in range(n):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j

        a[i], a[min] = a[min], a[i]

a = [55, 22, 33, 66, 11, 77, 0]
selection_sort(a)
print(a)
