a = [100, 180, 260, 310, 40, 535, 695]
n = len(a)
local_minima = []
local_maxima = []
print(n)
i=0
while(i<n+1):
    if a[i] < a[i+1]:
        
        local_minima.append(a[i])
    
    elif a[i] > a[i+1]:

        local_maxima.append(a[i])
        
    i += 1
    else:
        
        break

print(local_minima)
print(local_maxima)
