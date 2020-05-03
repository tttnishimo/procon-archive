n,d = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
res = 0
for i in range(n-1):
  for j in range(i+1,n):
    dist = 0
    for k in range(d):
      dist += (arr[i][k] - arr[j][k])**2
    if dist == float(int(pow(dist,1/2))**2):
      res += 1
print(res)