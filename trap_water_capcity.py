def trap_water(array):
    n = len(array)
    left_max = [0 for _ in range(n)]
    right_max = [0 for _ in range(n)]

    current_left_max = 0
    for i in range(n):
        current_left_max = max(current_left_max, array[i])
        left_max[i] = current_left_max

    current_right_max = 0
    for i in range(n-1, -1, -1):
        current_right_max = max(current_right_max, array[i])
        right_max[i] = current_right_max

    total = 0
    for i in range(n):
        # print(total)
        total += min(left_max[i], right_max[i]) - array[i]

    print(total)

a = [2, 1, 2]
# a = [3, 0, 1, 3, 0, 5]
trap_water(a)
