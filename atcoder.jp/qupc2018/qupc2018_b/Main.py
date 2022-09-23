for _ in range(int(input())):
  A,B,C=map(int,input().split())
  f=False
  if A%2:
    if B+C//10<10:
      f=True
    else:
      b=min(10,B)
      B-=b
      C-=(10-b)*10
  if B%2:
    if C<10:
      f=True
  if C%2 or f:
    print('No')
  else:
    print('Yes')