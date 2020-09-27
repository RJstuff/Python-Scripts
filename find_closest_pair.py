MAX_VAL = 1000000000
def find_pair(arr,n,x):
    res_l,res_r=0,0
    l = 0
    r = n-1
    diff = MAX_VAL

    while r>l:
        if abs(arr[l]+arr[r]-x)<diff:
            res_l=l
            res_r=r
            diff = abs(arr[l]+arr[r]-x)

        if arr[l]+arr[r] > x:
            r-=1

        else:
            l+=1

    print("the closest pair is ")
    print(arr[res_l])
    print(arr[res_r])

if __name__ == "__main__":
    arr = [10,22,28,29,30,40]
    n = len(arr)
    x = 54
    print(find_pair(arr,n,x))
    
