h,m=map(int,input().split())
while True:
  H='0'*(2-len(str(h)))+str(h)
  M='0'*(2-len(str(m)))+str(m)
  H,M=H[0]+M[0],H[1]+M[1]
  if int(H)<24 and int(M)<60:
    print(h,m)
    exit()
  m+=1
  if m==60:
    h+=1
    m=0
  if h==24:
    h=0