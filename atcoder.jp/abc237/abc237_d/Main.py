from collections import deque
N=int(input())
S=input()
d=deque([N])
for i in range(N):
  if S[-i-1]=='R':
    d.appendleft(N-i-1)
  else:
    d.append(N-i-1)
print(*d)