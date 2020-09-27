"""def MooreVote(arr):
    count = 1
    max_index = 0

    for i in range(len(arr)):
        if arr[max_index] == arr[i]:
            count += 1

        else:
            count -= 1

        if count == 0:
            count = 1
            max_index = i
            

    return arr[max_index]

def isMajority(arr,cand):
    count = 0
    for i in range(len(arr)):
        if arr[i] == cand:
            count += 1

        if count > len(arr)/2:
            return True
        else:
            return False

def printMajority(arr, n):
    cand = MooreVote(arr)
    if isMajority(arr, cand) == True:
        print(cand)

    else:
        print("No majority element exists !")

if __name__ == "__main__": 
    arr = [1, 1, 2, 1, 3, 5, 1] 
    n = len(arr) 
       
    printMajority(arr, n) """

def findMajority(arr):
    max_count = 0
    index = -1

    for i in range(len(arr)):
        count = 0

        for j in range(len(arr)):
            if (arr[i] == arr[j]):
                count += 1

        if (count > max_count):

            max_count = count
            index = i


    if(max_count > len(arr)/2):
        print(arr[index] ,"with number of occurences :",count)

    else:
        print("no majority element")

if __name__ == "__main__":
    arr = [1,1,2,1,3,5,1]
    findMajority(arr)







































