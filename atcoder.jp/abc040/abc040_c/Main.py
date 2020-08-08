n=int(input())
a=list(map(int,input().split()))
ans=[0,abs(a[1]-a[0])]
for i in range(2,n):
  ans.append(min(ans[i-2]+abs(a[i]-a[i-2]),ans[i-1]+abs(a[i]-a[i-1])))
print(ans[-1])