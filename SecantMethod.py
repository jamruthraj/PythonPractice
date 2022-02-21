def f(x):
    return 6*(x**2) - 10*x - 9


def secant(x0, x1, e, n):
    iter = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Divide by zero error!')
            break

        x2 = x0 * f(x1) - x1 * f(x0)/(f(x1) - f(x0))
        print('Iteration-%d, x2 = %0.4f and f(x2) = %0.4f' % (iter, x2, f(x2)))
        x0 = x1
        x1 = x2
        iter = iter + 1

        if iter > n:
            print('Not Convergent!')
            break

        condition = abs(f(x2)) > e
    print('After minimization, x = : %0.4f' % x2)


x0 = float(input('Enter Lower Bound: '))
x1 = float(input('Enter Upper Bound: '))
e = float(input('Maximum Error: '))
n = int(input('Maximum Iterations: '))


secant(x0, x1, e, n)
