from operaciones import sumar, dividir
import pytest

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)

print("test_operaciones.py creado")
