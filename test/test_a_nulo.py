from src.raiz_segundo_grado import raiz_segundo_grado
import pytest


@pytest.mark.a_nulo
def test_division_por_cero():
    assert raiz_segundo_grado(0, 1, 1) == None

@pytest.mark.a_nulo
def test_coeficientes_nulos():
    assert raiz_segundo_grado(0, 0, 0) == None