def ReduceToOne(arr):
    _size = len(arr)
    cost = (_size - 1) * min(arr)

    return cost



arr = [4,3,2]

ans = ReduceToOne(arr)
print(ans)

        
