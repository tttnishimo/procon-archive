n = int(input())
a = list(map(str, input().split()))
if a.count('Y') == 0:
  print('Three')
else:
  print('Four')