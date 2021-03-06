n=int(input())
k=int(input())
a=list(map(str,input().split()))
c=[0]*len(a)
for _ in range(n-1):
  l=int(input())
  b=list(map(str,input().split()))
  for i in b:
    if i in a:
      c[a.index(i)]+=1
print(sum([1 for i in range(len(a)) if c[i]==n-1]))