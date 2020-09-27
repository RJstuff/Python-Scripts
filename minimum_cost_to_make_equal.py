def Minimum_cost(arr):
    count_even = 0
    count_odd = 0
    _size = len(arr)
    for i in range(_size):
        if arr[i] % 2 == 0:
            count_even += 1

        else:
            count_odd += 1

    return min(count_even, count_odd)

arr = [2,2,2,2,5]
print(Minimum_cost(arr))
