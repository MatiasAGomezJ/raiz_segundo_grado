from src.raiz_segundo_grado import raiz_segundo_grado
import pytest


@pytest.mark.c_nulo
def test_c_nulo():
    assert raiz_segundo_grado(1, 1, 0) == (0, -1)

@pytest.mark.c_nulo
def test_c_nulo_raiz_nula():
    assert raiz_segundo_grado(2, 4, 0) == (0, -2)