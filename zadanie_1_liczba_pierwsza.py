def czy_jest_pierwsza(x) :


    for i in range(2,x) :
        if x % i == 0 :
            return False

    return True

assert czy_jest_pierwsza(11) == True
assert czy_jest_pierwsza(8) == False

def test_czy_jest_pierwsza_dla_liczby_pierwszej()
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(17) == True


