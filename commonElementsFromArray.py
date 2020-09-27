#find the common elements from 3 sorted arrays

def common(arr1,arr2,arr3,n1,n2,n3):
    i,j,k=0,0,0
    while(i<n1 and j<n2 and k<n3):
        if(arr1[i]==arr2[j] and arr2[j]==arr3[k]):
            print(arr1[i])
            i+=1
            j+=1
            k+=1
        elif(arr1[i]<arr2[j]):
            i+=1
        elif(arr2[j]<arr3[k]):
            j+=1

        else:
            k+=1

arr1 = [4,5,8,10]
arr2 = [1,4,8,12,23]
arr3 = [2,3,4,8,56,78,99]

n1 = len(arr1)
n2 = len(arr2)
n3 = len(arr3)

print(common(arr1,arr2,arr3,n1,n2,n3))
