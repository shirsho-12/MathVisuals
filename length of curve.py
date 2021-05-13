import sympy


def find_length(fx, variable, a, b):
    derivative = sympy.Derivative(fx, var).doit()
    length = sympy.Integral(sympy.sqrt(1 + derivative ** 2), (variable, a, b)).doit().evalf()
    return length


if __name__ == '__main__':
    func = input("Enter a one variable function: ")
    var = input("Enter variable: ")
    upper = float(input("Enter upper limit: "))
    lower = float(input("Enter lower limit: "))

    try:
        func = sympy.sympify(func)
    except sympy.SympifyError:
        print("Invalid input")
    else:
        var = sympy.Symbol(var)
        print('Length of {0} between {1} and {2} is: {3}'.format(func, upper, lower,
                                                                 find_length(func, var, upper, lower)))