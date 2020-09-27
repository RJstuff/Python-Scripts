rr = input

s = rr()

a = s.split('.')
a = list(map(int, a))
ans = 0

for x in a:
    ans += sum(map(int, str(x)))
print(ans)
