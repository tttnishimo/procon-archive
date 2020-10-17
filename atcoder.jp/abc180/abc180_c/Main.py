n=int(input())
a=[]
for i in range(1,int(n**0.5)+1):
  if n%i==0:
    print(i)
    if i!=n//i:
      a.append(n//i)
for i in range(len(a)):
  print(a[-i-1])