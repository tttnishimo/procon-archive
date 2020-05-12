import itertools
n,m = map(int, input().split())
a = [0]*(m+2)
sum_s = 0
for i in range(n):
  l,r,s = map(int,input().split())
  a[l] += s
  a[r+1] -= s
  sum_s += s
a = list(itertools.accumulate(a))
print(sum_s-min(a[1:-1]))