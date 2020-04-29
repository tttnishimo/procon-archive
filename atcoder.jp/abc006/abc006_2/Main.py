tribo = [0,0,1]
for i in range(10**6):
  tribo.append((tribo[-1] + tribo[-2] + tribo[-3])%10007)
n = int(input())
print(tribo[n-1])