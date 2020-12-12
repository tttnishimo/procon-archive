n=int(input())
a=list(map(int,input().split()))
ans=[sum(a)-2*sum(a[1::2])]
for i in range(n-1):
  ans.append(2*a[i]-ans[-1])
print(*ans)