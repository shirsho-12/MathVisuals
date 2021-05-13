import sympy

print("McLaurin expansion of sin(x)")

x = sympy.Symbol('x')


def series(x):
    val = int(input("Enter number of terms: "))
    series = x
    for i in range(1, val + 1):
        if i % 2 == 1:
            series -= x ** (i*2 + 1)/ sympy.factorial(i*2 + 1)
        else:
            series += x ** (i * 2 + 1) / sympy.factorial(i * 2 + 1)

    sympy.pprint(series, order='rev-lex')
    graph = sympy.plot(series, title="graph of sin(x) using the first 50 terms of the McLaurin Series")
    graph.save('mclaurin-series-sin_x.png')
    #graph.show()

if __name__ == '__main__':
    series(x)
