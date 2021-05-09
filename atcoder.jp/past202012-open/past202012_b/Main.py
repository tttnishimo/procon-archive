n=int(input())
s=input()
t=''
for i in range(n):
  if t.count(s[-i-1])==0:
    t=s[-i-1]+t
print(t)