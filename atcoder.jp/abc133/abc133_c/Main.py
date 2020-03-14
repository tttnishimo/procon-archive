l,r = map(int, input().split())
if r - l > 2018:
  print(0)
else:
  a = []
  min_a = 10**9
  for i in range(r-l+1):
    a.append((l+i)%2019)
  for i in range(len(a)):
    for j in range(1,len(a)-i):
      min_a = min(min_a,(a[i]*a[i+j])%2019)
#      print(i,j,(a[i]*a[i+j])%2019)
  print(min_a)