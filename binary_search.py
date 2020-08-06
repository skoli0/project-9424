def binary_search_r(a, low, high, target):
    if low > high:
        return False
    else:
        mid = low + (high - low) // 2 # (low+high)/2 could result overflow in low level programming languages
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            return binary_search_r(a, mid+1, high, target)
        else:
            return binary_search_r(a, low, mid-1, target)

def binary_search(a, target):
    low = 0
    high = len(a)

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

a = [_**2 for _ in range(10)]
print(a)
target = 25

print(f"{target} found at {binary_search(a, target)}")
print(f"{target} found at {binary_search_r(a, 0, len(a), target)}")
