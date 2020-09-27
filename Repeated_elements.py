#find duplicates from a list

def Repeat(arr):
    _size = len(arr)
    r = []
    for i in range(_size):
        k = i+1
        for j in range(k, _size):
            if arr[i] == arr[j] and arr[i] not in r:
                r.append(arr[i])
    return r

arr = [10,20,10,-30,20,30]
ans = Repeat(arr)
print(ans)
                
