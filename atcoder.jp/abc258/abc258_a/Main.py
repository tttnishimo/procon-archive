K=int(input())
print(str(21+K//60)+':'+'0'*(1-(K%60)//10)+str(K%60))