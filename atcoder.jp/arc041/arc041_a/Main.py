a,b = map(int, input().split())
n = int(input())
if b >= n:
  print(a+n)
else:
  print(a+2*b-n)
