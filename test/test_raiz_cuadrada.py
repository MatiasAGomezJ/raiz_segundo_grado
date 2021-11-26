from src.raiz_segundo_grado import raiz_segundo_grado
import pytest


@pytest.mark.discriminante
def test_discriminante_cero():
    assert raiz_segundo_grado(1, 2, 1) == (-1, -1)


@pytest.mark.discriminante
def test_discriminante_positivo():
    assert raiz_segundo_grado(1, -1, -2) == (2, -1)


@pytest.mark.discriminante
def test_discriminante_negativo():
    assert raiz_segundo_grado(1, 1, 1) == None


@pytest.mark.discriminante
def test_soluciones_fraccion():
    assert raiz_segundo_grado(6, -7, 2) == (2 / 3, 1 / 2)