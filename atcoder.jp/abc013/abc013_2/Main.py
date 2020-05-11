a1 = '0123456789'
a2 = '5678901234'
n = input()
m = input()
print(min(abs(a1.index(n) - a1.index(m)),abs(a2.index(n) - a2.index(m))))