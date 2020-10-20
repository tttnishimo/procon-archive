t=int(input())
a='atcoder'
for _ in range(t):
  s=input()
  n=len(s)
  if s>a:
    print(0)
  elif n==s.count('a'):
    print(-1)
  else:
    for i in range(n):
      if s[i]!='a':
        if s[i]>'t':
          print(i-1)
        else:
          print(i)
        break