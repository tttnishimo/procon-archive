n = int(input())
arr = []
for i in range(n):
  a,b = map(str, input().split())
  arr.append([a,-int(b),i+1])
arr.sort()
for a,b,i in arr:
  print(i)