from entities import Point, Triangle


def generate():
    p1 = Point(0.0, 0.0, 0.0)
    p2 = Point(1.0, 0.0, 0.0)
    p3 = Point(1.0, 0.0, 1.0)
    p4 = Point(0.0, 0.0, 1.0)
    p5 = Point(0.0, 1.0, 0.0)
    p6 = Point(1.0, 1.0, 0.0)
    p7 = Point(1.0, 1.0, 1.0)
    p8 = Point(0.0, 1.0, 1.0)

    """ p1 = Point(-.5, -.5, -.5)
    p2 = Point(.5, -.5, -.5)
    p3 = Point(.5, -.5, .5)
    p4 = Point(-.5, -.5, .5)
    p5 = Point(-.5, .5, -.5)
    p6 = Point(.5, .5, -.5)
    p7 = Point(.5, .5, .5)
    p8 = Point(-.5, .5, .5) """

    t1 = Triangle(p1.copy(), p2.copy(), p3.copy())
    t2 = Triangle(p1.copy(), p3.copy(), p4.copy())
    t3 = Triangle(p1.copy(), p6.copy(), p2.copy())
    t4 = Triangle(p1.copy(), p5.copy(), p6.copy())
    t5 = Triangle(p3.copy(), p2.copy(), p6.copy())
    t6 = Triangle(p3.copy(), p6.copy(), p7.copy())
    t7 = Triangle(p1.copy(), p4.copy(), p5.copy())
    t8 = Triangle(p4.copy(), p8.copy(), p5.copy())
    t9 = Triangle(p4.copy(), p3.copy(), p7.copy())
    t10 = Triangle(p4.copy(), p7.copy(), p8.copy())
    t11 = Triangle(p5.copy(), p8.copy(), p7.copy())
    t12 = Triangle(p5.copy(), p7.copy(), p6.copy())

    trigs = [
        t1, t2, t3, t4, t5, t6,
        t7, t8, t9, t10, t11, t12
    ]
    return trigs
