divisors = []
def Solve(n):
    i = 1
    while i < n:
        if n%i == 0:
            divisors.append(i)
 
        i += 1
            
out = Solve(28)
print(out)
