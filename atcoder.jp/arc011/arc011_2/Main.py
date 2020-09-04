n=int(input())
s=input().split()
ans=[]
for i in s:
  tmp=''
  i=i.lower()
  for j in list(i):
    if j=='b' or j=='c':
      tmp+='1'
    elif j=='d' or j=='w':
      tmp+='2'
    elif j=='t' or j=='j':
      tmp+='3'
    elif j=='f' or j=='q':
      tmp+='4'
    elif j=='l' or j=='v':
      tmp+='5'
    elif j=='s' or j=='x':
      tmp+='6'
    elif j=='p' or j=='m':
      tmp+='7'
    elif j=='h' or j=='k':
      tmp+='8'
    elif j=='n' or j=='g':
      tmp+='9'
    elif j=='z' or j=='r':
      tmp+='0'
  if tmp!='':
    ans.append(tmp)
print(*ans)