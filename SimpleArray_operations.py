#searching in array(unsorted)
def search(arr,n,key):
    n = len(arr)
    for i in range(n):
        if(arr[i]==key):
            return i
    return -1

arr = [40,12,34,86,99]
key = 3
n = len(arr)

index = search(arr,n,key)

if index!=-1:
    print("element found at position "+str(index))

else:
    print("not found")
"""
#insertion
def insert(arr,element):
    arr.append(element)

arr = [12,24,2,4,23]
ans = insert(arr,100)
print(arr)

#deletion
def delete(arr,ele):
    arr.remove(ele)

arr = [1,2,3]
delete(arr,2)
print(arr)
"""
    

    
