Q=int(input())
S=[]
for i in range(Q):
  s=input()
  if s=='READ':
    print(S.pop())
  else:
    S.append(s)