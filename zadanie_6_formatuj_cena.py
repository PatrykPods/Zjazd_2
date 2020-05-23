def formatuj(*args, **kwargs :
    text = "\n".join(args)
    for znacznik, wartosc in kwargs.items():
        text = text.replace("$" + znacznik, str(wartosc))
    return text



def test_formatuj() :
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena = 10) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('$cena', '$cena', cena = 15) == '15 \n15'