n=int(input())
a=[]
ans=0
for i in range(n):
  a.append(int(input()))
for i in range(1,len(str(max(a)))):
  if [a[j] % 10**i for j in range(n)].count(0) == n:
    ans += 1
  else:
    break
print(ans)