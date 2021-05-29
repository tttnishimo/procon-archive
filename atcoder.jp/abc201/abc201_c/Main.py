S=input()
ans=0
for i in range(10):
  for j in range(10):
    for k in range(10):
      for l in range(10):
        flg=0
        for m,s in enumerate(S):
          if s=='o':
            if m not in [i,j,k,l]:
              flg=1
          elif s=='x':
            if m in [i,j,k,l]:
              flg=1
        if flg==0:
          ans+=1
print(ans)