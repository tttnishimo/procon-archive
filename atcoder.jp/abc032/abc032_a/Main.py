import fractions
import math
a=int(input())
b=int(input())
c=int(input())
lcm = (a * b) // fractions.gcd(a,b)
print(lcm * math.ceil(c / lcm))