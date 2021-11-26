from src.raiz_segundo_grado import raiz_segundo_grado
import pytest


@pytest.mark.b_c_nulo
def test_raiz_nula_unica():
    assert raiz_segundo_grado(1, 0, 0) == 0 