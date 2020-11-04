n=int(input())
a=[]
for i in range(n):
  s=input()
  b=int(s[:4])
  b-=b%5
  b=b//100*12+b%100//5
  c=int(s[-4:])
  if c%5!=0:
    c+=5-c%5
  c=c//100*12+c%100//5
  a.append([b,c])
a.sort()
l=a[0][0]
r=a[0][1]
for i in range(1,len(a)):
  if a[i][0]<=r and a[i][1]>r:
    r=a[i][1]
  elif a[i][0]>r:
    tmp=str(l//12*100+l%12*5)
    tmp='0'*(4-len(tmp))+tmp
    tmp2=str(r//12*100+r%12*5)
    tmp2='0'*(4-len(tmp2))+tmp2
    print(tmp+'-'+tmp2)
    l=a[i][0]
    r=a[i][1]
tmp=str(l//12*100+l%12*5)
tmp='0'*(4-len(tmp))+tmp
tmp2=str(r//12*100+r%12*5)
tmp2='0'*(4-len(tmp2))+tmp2
print(tmp+'-'+tmp2)