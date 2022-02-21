import numpy as np


cods = input("Enter the point coordinates: ").split(" ")
xcod, ycod = int(cods[0]), int(cods[1])

cods = input("Enter coordinates of a point on the line: ").split(" ")
x1, y1 = int(cods[0]), int(cods[1])
cods = input("Enter coordinates of another point on the line: ").split(" ")
x2, y2 = int(cods[0]), int(cods[1])


def slope_form(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    b = y1-(m*x1)
    return m, b


line = slope_form(x1, y1, x2, y2)
m = line[0]
b = line[1]
x = (x1, x2)
y = (y1, y2)


def calc_fx(m, b, x):
    fx = m*x+b
    return fx


def distance(x1, y1, x2, y2):
    d = np.sqrt((x1-x2)**2+(y1-y2)**2)
    return d


def check_pos(x1, x2):
    if x2 < x1:
        pos = 'right'
    else:
        pos = ''
    return pos


def next_iter(xl, xu):
    d = 0.618*(xu-xl)
    x1 = xl+d
    x2 = xu-d
    return x1, x2


def new_range(xl, xu, x1, x2, pos):
    y1 = calc_fx(m, b, x1)
    y2 = calc_fx(m, b, x2)
    fx1 = distance(xcod, ycod, x1, y1)
    fx2 = distance(xcod, ycod, x2, y2)
    if fx2 > fx1 and pos == 'right':
        xl = x2
        xu = xu
        new_x = next_iter(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x1
    else:
        xl = xl
        xu = x1
        new_x = next_iter(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        xopt = x2
    return xl, xu, xopt, fx1, fx2


def golden_search(xl, xu, mode, et):
    it = 0
    e = 1
    while e >= et:
        new_x = next_iter(xl, xu)
        x1 = new_x[0]
        x2 = new_x[1]
        fx1 = calc_fx(m, b, x1)
        fx2 = calc_fx(m, b, x2)
        pos = check_pos(x1, x2)
        if mode == 'min':
            new_boundary = new_range(xl, xu, x1, x2, pos)
        else:
            print('Please define min/max mode')
            break
        xl = new_boundary[0]
        xu = new_boundary[1]
        xopt = new_boundary[2]
        distance_1 = new_boundary[3]
        distance_2 = new_boundary[4]
        mean_distance = (distance_1+distance_2)/2

        it += 1
        print('Iteration: ', it)
        r = (np.sqrt(5)-1)/2
        e = ((1-r)*(abs((xu-xl)/xopt)))*100
        print('Error:', e)
        print('distance 1=', distance_1)
        print('distance 2=', distance_2)
        print('mean distance=', round(mean_distance, 3))


cods = input("Enter the intial start points: ").split(" ")
xsl, xsu = int(cods[0]), int(cods[1])
err = float(input("Enter the maximum error: "))
golden_search(xsl, xsu, 'min', err)
