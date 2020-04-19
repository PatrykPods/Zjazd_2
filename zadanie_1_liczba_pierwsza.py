def czy_jest_pierwsza(x) :
    i = 0

    for i in range(2,(x - 1)) :
        if x % i == 0 :
            print("false")
            return "false"
        else :
            print("true")
            return "true"

czy_jest_pierwsza(8)
