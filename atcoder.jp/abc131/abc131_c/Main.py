import fractions
a,b,c,d = map(int, input().split())
print(b - b//c- b//d + b//(c*d//fractions.gcd(c,d)) - (a-1 - (a-1)//c- (a-1)//d + (a-1)//(c*d//fractions.gcd(c,d))))