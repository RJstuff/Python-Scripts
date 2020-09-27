"""
 1......   a = input("enter a string : ")

if a[::-1] == a:
    print("input string is pallingdrome !")
else:
    print("not a pallingdrome")
 
        2......     def common(a,b):
    print(set(a) & set(b))
            
list_1 = int(input("enter the size of list 1 :"))
A = []
for i in range(list_1):
    k = input("")
    A.append(k)

list_2 = int(input("enter the size of 2nd list :"))
B = []
for j in range(list_2):
    l = input("")
    B.append(l)   

print(common(A,B))

      3....   a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

A = []

for i in range(len(a)):
    if a[i]%2 == 0:
        A.append(a[i])
    else:
        i+=1
print(a)
print(A)
print(a[::-2])

  4........        def new_list(old):
    o = set(old)
    return o
a = [1,2,1,3,4,1]
print(new_list(a))


  5..........     def updated_list(a):
    A = []
    A.append(a[0])
    A.append(a[-1])
    return A
l = [12,3,4,12,4,1,3]
print(updated_list(l))

  6.........  a = int(input("Enter a number : "))
n1 = 0
count = 0
n2 = 1
while True:
    
    if(a<0):
       print("enter a positive number")
       break
    elif(a==1):
        print("1")
        break
    else:
        while count<a:
            print(n1,end=' , ')
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        break
"""


   
        

        
    
    


























