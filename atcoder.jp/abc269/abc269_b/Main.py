S=[input() for _ in range(10)]
a=-1
b=10
for i in range(10):
  if a==-1 and '#' in S[i]:
    a=i+1
    c=S[i].index('#')+1
    d=c+S[i].count('#')-1
  if a!=-1 and b==10 and '#' not in S[i]:
    b=i
print(a,b)
print(c,d)