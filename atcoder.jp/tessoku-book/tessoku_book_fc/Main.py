N=bin(int(input())-1)[2:]
N='0'*(10-len(N))+N
N=N.replace('0','4')
N=N.replace('1','7')
print(N)