n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
a.append(0)
s=0
for i in range(1,n+2):
  s += abs(a[i]-a[i-1])
for i in range(1,n+1):
  if a[i-1] <= a[i] <= a[i+1] or a[i-1] >= a[i] >= a[i+1]:
    print(s)
  else:
    print(s-2*min(abs(a[i-1]-a[i]),abs(a[i]-a[i+1])))