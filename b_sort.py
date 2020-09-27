def b_sort(arr):
        for i in range(len(arr)-1,):
               if arr[i]>arr[i+1]:
                                temp = arr[i]
                                arr[i] = arr[i+1]
                                arr[i+1] = temp 
                
                        

a = [123,12,23,41,1]
print(a)
b_sort(a)

print(a)
