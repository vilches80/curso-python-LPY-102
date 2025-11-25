def invertir(t):
    return t[::-1]

def mayus(t):
    return t.upper()

def palabra_mas_larga(t):
    return max(t.split(), key=len)