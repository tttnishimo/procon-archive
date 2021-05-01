A,B,C,D,E,F=map(int,input().split())
ans=[100*A,0]
con=0.0
a={A*100*i+B*100*j for i in range(31) for j in range(31)}
b={C*i+D*j for i in range(F//100*E//C+2) for j in range(F//100*E//D+2)}
a.discard(0)
for i in a:
  for j in b:
    if i+j<=F and j/i<=E/100:
      if j/(i+j)>con:
        con=j/(i+j)
        ans=[i+j,j]
print(*ans)