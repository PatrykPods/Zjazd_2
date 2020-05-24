def square_area(a):
    if a > 0:
        return a*a
    else:
        return("nieprawidłowa długość boku [0/<0]")


def triangle_area(a,h):
    if a > 0 and h > 0:
        return (a*h)/2
    else:
        return("nieprawidłowe dane")


square_area(-3)
triangle_area(3,4)
triangle_area(0,4)