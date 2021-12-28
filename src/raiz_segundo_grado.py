from math import sqrt

def raiz_segundo_grado(a, b, c):
    if a == 0:
        return None

    if b == c == 0:
        return 0
        
    if b == 0:
        if a == c:
            return None
        return (abs(c//a), c//a)

    if c == 0:
        return 0, -(b//a)

    lo_que_hay_dentro_de_la_raiz_cuadrada = b ** 2 - 4 * a * c
    if lo_que_hay_dentro_de_la_raiz_cuadrada >= 0:
        x = (-b + sqrt(lo_que_hay_dentro_de_la_raiz_cuadrada)) / (2 * a)
        y = (-b - sqrt(lo_que_hay_dentro_de_la_raiz_cuadrada)) / (2 * a)
        return x, y
    else:
        return None