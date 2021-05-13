from sympy import FiniteSet, pi, sqrt


def time(length, g):
    T = 2*pi * sqrt(length/g)
    return T


L = FiniteSet(15, 18, 21, 22.5, 25)
g_set = FiniteSet(9.78, 9.8, 9.83)

print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))

for elem in L*g_set:
    t = time(elem[0]/100, elem[1])
    
    print('{0:^15}{1:^15}{2:^15.3f}'.format(float(elem[0]), float(elem[1]), float(t)))
