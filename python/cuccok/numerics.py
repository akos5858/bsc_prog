from numpy import sign, sqrt

def newton(x, x0, eps=1e-14, max_steps=100) -> tuple:

    def f(a):          
        return a**2 - x
    def df(a):
        return 2*a   

    steps = 0 
    
    for i in range(max_steps):
        y = f(x0)
        dy = df(x0)

        x1 = x0 - y / dy                

        if abs(x1 - x0) <= eps:   
            return x1, steps                  
        else:
            x0 = x1   
            steps += 1         

    return print("wrong guess")


def bisection(f, interval: list, eps=1e-14, max_steps=10000) -> tuple:
    
    a, b = interval[0], interval[1]
    steps = 0

    while abs(b-a) > eps and steps < max_steps:
        c = (a+b)/2
        if sign(f(c)) == sign(f(a)):
            a = c
            steps += 1
        else:
            b = c
            steps += 1
     
    return c, steps


if __name__ == '__main__':
    r_newton = newton(2, 1)
    r_bisection = bisection(lambda x : x**2 - 2, [1, 2])
    print(r_newton)
    print(r_bisection)
    #print(bisection(lambda x : x**3, [-0.5, 1], eps=1e-1000))


