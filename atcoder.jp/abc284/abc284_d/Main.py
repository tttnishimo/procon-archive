for _ in range(int(input())):
  N=int(input())
  for i in range(2,int(N**(1/3))+1):
    if N%i==0:
      N//=i
      if N%i==0:
        print(i,N//i)
      else:
        print(int(N**.5),i)