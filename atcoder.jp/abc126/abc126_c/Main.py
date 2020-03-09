import math
tmp = 0
big_dice = 0
a,b = map(int, input().split())
log2_b = math.log2(b)
if a > b:
  c = b
  big_dice = (a - b) / a
else:
  c = a
for i in range(1, c + 1):
  log2_i = math.log2(i)
  n = math.ceil(log2_b - log2_i)
  tmp = tmp + 0.5**n
print(tmp / a + big_dice)