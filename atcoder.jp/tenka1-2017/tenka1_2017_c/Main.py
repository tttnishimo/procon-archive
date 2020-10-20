N=int(input())
for h in range(1,3501):
  for n in range(1,3501):
    if 4*h*n-N*n-h*N>0:
      if N*h*n%(4*h*n-N*n-h*N)==0:
        print(h,n,N*h*n//(4*h*n-N*n-h*N))
        exit()