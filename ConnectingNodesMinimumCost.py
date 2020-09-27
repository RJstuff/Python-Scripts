def ConnectNodes(arr):
    minimum = min(arr)
    print(minimum)
    cost = 0
    for i in arr:
        if i == minimum:
            pass
        else:
            cost += i * minimum

    return cost

arr = [4,3,2,5]
ans = ConnectNodes(arr)
print(ans)
