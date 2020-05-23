def policz_znaki(text, a = "<", b = ">") :
    zliczaj = 0
    licznik = 0

    for znak in text :
        if znak == a :
            zliczaj += 1
            continue
        elif znak == b :
            zliczaj -= 1
            continue

        licznik += zliczaj

print(policz_znaki("<a<a<a>>>>", "<", ">"))




def test_policz_znaki() :
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala ma <ko> a kot ma ale') == 2
    assert policz_znaki('ala ma [kota] a [kot] ma ale , "[", "]') == 7
    assert policz_znaki('a <a<a<a>>>>') == 6