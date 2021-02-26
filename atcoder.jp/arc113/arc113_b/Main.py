a,b,c=map(int,input().split())
n=a%10
t=[n]
while True:
  n*=a
  n%=10
  if t[0]!=n:
    t.append(n)
  else:
    break
print(t[pow(b,c,len(t))-1])