from re import X
import main

def test_dodawanie():
    assert main.dodawanie(7, 7) == 14
    assert main.dodawanie(9, 9) == 18
    assert main.dodawanie(10, 10) == 20

def test_sprawdzenie():
    assert main.sprawdzenie(6, 2) == 6
    assert main.sprawdzenie(9, 11) == 'x musi byc wieksze od y'
