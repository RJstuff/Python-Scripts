#arr[] =  [-6, -3, -1, 2, 4, 5]
def swap(a,b):
    a=b
    b=a
    return (a,b)
def sortSquare(arr,n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]

    for j in range(n):
        if arr[j] < arr[j+1]:
            swap(arr[j],arr[j+1])
                
        

arr =  [-6, -3, -1, 2, 4, 5]
n = len(arr)
print("Original array : ", arr)
sortSquare(arr,n)
print("after sortSquare : ")
for i in range(n):
    print(arr[i],end = ' ')
