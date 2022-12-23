D=int(input())
A=[int(input()) for _ in range(D)]
ac=[0]
for a in A:
  ac.append(ac[-1]+a)
for _ in range(int(input())):
  S,T=map(int,input().split())
  s=ac[S]
  t=ac[T]
  if t>s:
    print(T)
  elif t<s:
    print(S)
  else:
    print('Same')