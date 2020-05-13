n = int(input())
ans = 0
for i in range(int(pow(n,1/2))+1):
  if i**2 <= n:
    ans = i**2
print(ans)
