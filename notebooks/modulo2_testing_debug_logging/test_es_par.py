from operaciones import es_par
import pytest

def test_es_par():
   assert es_par(1) == False

@pytest.mark.parametrize("a,resultado", [
        (1, False),
        (2, True),
        (0, True),
        (100, True)
        #("Cadena", False)
    ])
def test_es_par_parametrizado(a,resultado):
  assert es_par(a) == resultado