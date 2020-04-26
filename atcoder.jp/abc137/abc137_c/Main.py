n = int(input())
a = {}
for i in range(n):
  tmp = "".join(sorted(input()))
  if tmp in a:
    a[tmp] += 1
  else:
    a[tmp] = 1
res = [i*(i-1)//2 for i in a.values()]
print(sum(res))
