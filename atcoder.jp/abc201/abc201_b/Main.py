N=int(input())
a=[]
for _ in range(N):
  s,t=map(str,input().split())
  a.append([int(t),s])
a.sort()
print(a[-2][1])