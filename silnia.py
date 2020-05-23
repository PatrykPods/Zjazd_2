def silnia(n):
    if n < 0:
        return'error'
    elif n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(5))


def test_silnia() :
    assert silnia(5) == 120
    assert silnia(0) == 1
    assert silnia(3) == 6