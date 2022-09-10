from entities import Point, Triangle


def generate():
    L = 1

    p1 = Point(0.0, 0.0, 0.0)
    p2 = Point(L/2, 0.0, L/2*3**0.5)
    p3 = Point(L, 0.0, 0.0)
    p4 = Point(L/2, L, L/6*3**0.5)

    t1 = Triangle(p1, p2, p3)
    t2 = Triangle(p1, p4, p2)
    t3 = Triangle(p1, p3, p4)
    t4 = Triangle(p2, p4, p3)

    trigs = [t1, t2, t3, t4]
    return trigs
