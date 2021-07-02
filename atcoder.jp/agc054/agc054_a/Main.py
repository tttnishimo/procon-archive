N=int(input())
S=input()
ans=0
while len(S)>1:
  i=-1
  T=S
  while i>-len(S)-1:
    if S[0]==S[i]:
      if i==-1:
        i-=1
      i-=1
    else:
      S=S[i+1:]
      ans+=1
      if i==-1:
        print(ans)
        exit()
      break
  if T==S:
    print(-1)
    exit()
print(ans)