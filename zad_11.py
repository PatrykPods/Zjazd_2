elementy = ["aaa", "aaaaa", "aba", "aba", "aaa", "ababa"]

elementy_2 = {"aaa", "aba",  "ccc"}

elementy = set(elementy)

print(f"liczba unikalnych elementow to: {len(elementy)}")
print(f"czesc wspolna zbiorow to: {elementy & elementy_2 } ")