N=int(input())
S=[]
for i in range(N):
  s=input()
  t=int(s)
  u=-(len(s)-len(str(int(s))))
  S.append([s,t,u])
S.sort(key=lambda x:(x[1],x[2]))
print(*[i[0] for i in S],sep='\n')