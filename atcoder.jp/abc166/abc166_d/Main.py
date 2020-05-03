n = int(input())
arr = []
for i in range(1,int(pow(n,1/2))+1):
  if n % i == 0:
    arr.append(i)
res = []
for i in range(len(arr)):
  for j in range(-arr[i]-1,int(pow(n,1/2)+1)):
    if (j + arr[i])**5 - j**5 == n:
      res = [j+arr[i],j]
      break
print(*res)