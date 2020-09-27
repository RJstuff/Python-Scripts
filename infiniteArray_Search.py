#given a array of infinite length , perform searching if array is sorted

#1. perform binary search, 2nd step because we need to find the boundary of array(limit)
def binary_search(arr,l,r,x):
    if r>=l:
        mid=l+(r-l)//2
        if arr[mid]==x:
            return mid
        if arr[mid]>x:
            return binary_search(arr,l,mid-1,x)
        return binary_search(arr,mid+1,r,x)
    return -1

#2.to find position ,create 2 indices high ,low
def findPos(a,key):
    low=0 #low
    h=1 #high
    val=a[h]

    while val<key:
        low=h
        h=2*h
        val=a[h]

    return binary_search(a,low,h,key)

#3. Main
a = [4,6,7,9,12,14,17,23,56,99]
ans = findPos(a,23)
if ans == -1:
    print("not found")
else:
    print("position")
    print(ans)




