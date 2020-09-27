import sys

def Triplet(arr,x):
    arr.sort()
    closetSum = sys.maxsize
    
    print(closetSum)
    for i in range(len(arr)-2):
        ptr1 = i+1;
        ptr2 = len(arr)-1
        
        
    while(ptr1<ptr2):
        sumS = arr[i]+arr[ptr1]+arr[ptr2]
        if(abs(x-sumS)<abs(x-closetSum)):
            closetSum = sumS
            if(sumS>x):
                ptr2-=1
            else:
                ptr1+=1

                
            return closetSum


if __name__ == "__main__":
    
    arr = [-1,2,1,-4];
    x = 1;
    print(Triplet(arr,x));
