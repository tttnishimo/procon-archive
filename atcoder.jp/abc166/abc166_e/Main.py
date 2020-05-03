n = int(input())
a = list(map(int, input().split()))
res = 0
dict = {}
dict[a[0]+1] = 1
for i in range(1,n):
  res += dict.get(i+1-a[i],0)
  dict[a[i]+i+1] = dict.get(a[i]+i+1,0) + 1
print(res)
