S=input()
al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nu='0123456789'
if len(S)==8:
  if S[0] in al and S[-1] in al:
    if S[1] in nu and S[2] in nu and S[3] in nu and S[4] in nu and S[5] in nu and S[6] in nu:
      if str(int(S[1:-1]))==S[1:-1]:
        print('Yes')
        exit()
print('No')