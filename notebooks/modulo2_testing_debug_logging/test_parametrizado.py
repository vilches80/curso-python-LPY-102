import pytest
from operaciones import sumar, dividir

@pytest.mark.parametrize("a,b,resultado", [
    (1, 1, 2),
    (2, 3, 5),
    (-5, 5, 0)
])
def test_sumar_parametrizado(a, b, resultado):
    assert sumar(a, b) == resultado

@pytest.mark.parametrize("a,b,resultado", [
    (1, 1, 1),
    (6, 2, 3),
    (-5, 5, -1)
    #(4, 0, ZeroDivisionError)
])
def test_dividir_parametrizado(a, b, resultado):
    assert dividir(a, b) == resultado

#print("test_parametrizado.py creado")
