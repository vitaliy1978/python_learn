from typing import List, Optional

n = "hello hi hello"

def first_repeated_word(n) -> str:
    """ Находит первый дубль в строке """
    n = n.split()
    d: Optional[str] = None
    for i in range(len(n)):
        if n.count(n[i]) > 1 and n[i] in n[0:i]:
            d = n[i]
            break
    return d

print(first_repeated_word(n))
