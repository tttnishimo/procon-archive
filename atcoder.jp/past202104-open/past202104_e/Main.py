from collections import deque
d=deque()
N=int(input())
S=input()
for i in range(N):
  if S[i]=='L':
    d.appendleft(i+1)
  elif S[i]=='R':
    d.append(i+1)
  elif S[i]=='A':
    if len(d)<1:
      print('ERROR')
    else:
      l=d.popleft()
      print(l)
  elif S[i]=='B':
    if len(d)<2:
      print('ERROR')
    else:
      l=d.popleft()
      m=d.popleft()
      print(m)
      d.appendleft(l)
  elif S[i]=='C':
    if len(d)<3:
      print('ERROR')
    else:
      l=d.popleft()
      m=d.popleft()
      n=d.popleft()
      print(n)
      d.appendleft(m)
      d.appendleft(l)
  elif S[i]=='D':
    if len(d)<1:
      print('ERROR')
    else:
      l=d.pop()
      print(l)
  elif S[i]=='E':
    if len(d)<2:
      print('ERROR')
    else:
      l=d.pop()
      m=d.pop()
      print(m)
      d.append(l)
  elif S[i]=='F':
    if len(d)<3:
      print('ERROR')
    else:
      l=d.pop()
      m=d.pop()
      n=d.pop()
      print(n)
      d.append(m)
      d.append(l)