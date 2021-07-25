N=int(input())
ans=0
i=1
if N<=52:
  print(N//2*3+N%2)
else:
  while True:
    if N<=26**i:
      print(ans+N*i)
      exit()
    else:
      ans+=26**i*i
      N-=26**i
      i+=1