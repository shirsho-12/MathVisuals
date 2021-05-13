
x = int(input("Enter number: "))
y = int(input("Enter number of multiples: "))

for i in range(1, y+1):
    print('{0} x {1} = {2}'.format(x, i, x*i))


from fractions import Fraction

a, b = map(Fraction, input().split())

print(a+b, a*b, a-b, a/b)