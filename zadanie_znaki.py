def zliczanie(text, counter) :
    zbior = set()
    for znak in set(text) :
        if text.count(znak) > counter :
            zbior.add(znak)
    return zbior


print(zliczanie("aaaaa bbbb ccccc", 4))



def test_test_wiecej_niz_dla_pustego_napisu() :
    assert zliczanie("", 0) == set()
def test_wiecej_niz_dla_niepustego_napis() :
    assert zliczanie("aaaaa bbbbb eeee ttttttt jjjjjjjjjjjj", 7) == {'t', 'j'}