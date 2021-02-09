n=int(input())
if sum([1 for _ in range(n) if input()=='black'])>n//2:
  print('black')
else:
  print('white')