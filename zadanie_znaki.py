def zliczanie(text, counter) :
    znaki = dict()
    znaki_2 = set()
    for x in text :
        if x in znaki :
            znaki[x] = znaki[x] + 1
        else :
            znaki[x] = 1

        if znaki[x] > counter :
            znaki_2.add(x)

    return znaki_2


print(zliczanie("aaaaa bbbb ccccc", 4))



def test_test_wiecej_niz_dla_pustego_napisu() :
    assert zliczanie("", 0) == set()
def test_wiecej_niz_dla_niepustego_napis() :
    assert zliczanie("aaaaa bbbbb eeee ttttttt jjjjjjjjjjjj", 7) == {'t', 'j'}