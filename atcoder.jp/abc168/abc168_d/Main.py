N,M=list(map(int,input().split()))
 
g=[[] for i in range(N+1)]
 
for i in range(M):
	a,b=list(map(int,input().split()))
	g[a].append(b)
	g[b].append(a)
 
from collections import deque
 
queue = deque([1])
d = [None] * (N+1)
while queue:
	v = queue.popleft()
	for i in g[v]:
		if d[i] is None:
			d[i] = v
			queue.append(i)
 
print("Yes")
print(*d[2:],sep='\n')