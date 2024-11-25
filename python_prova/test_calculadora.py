from calculadora import Calculadora

# somar --------------

def somar(a, b):
        return a + b

def test_somar():
    assert somar(1, 1) == 2
    assert somar(2, 2) == 4
    assert somar(3, 3) == 6


def test_somar_negativo():
    assert somar(-1, -1) == -2
    assert somar(-2, -2) == -4
    assert somar(-3, -3) == -6  

# subtrair --------------
def subtrair(a, b):
        return a - b

def test_subtrair():
    assert subtrair(4, 2) == 2
    assert subtrair(2, 2) == 0
    assert subtrair(4, 3) == 1


def test_subtrair_negativo():
    assert subtrair(-1, -1) == 0
    assert subtrair(-2, -2) == 0 
    assert subtrair(-3, -3) == 0 



# multiplicar --------------
def multiplicar(a, b):
        return a * b

def test_multiplicar():
    assert multiplicar(1, 2) == 2
    assert multiplicar(1, 1) == 1
    assert multiplicar(2, 2) == 4


def test_multiplicar_negativo():
    assert multiplicar(-1, -2) == 2
    assert multiplicar(-2, -2) == 4 
    assert multiplicar(-1, -1) == 1 



# dividir --------------
def dividir(a, b):
        return a / b

def test_dividir():
    assert dividir(4, 2) == 2
    assert dividir(8, 2) == 4
    assert dividir(10, 2) == 5


def test_dividir_negativo():
    assert dividir(-1, -1) == 1
    assert dividir(-2, -2) == 1  
    assert dividir(-3, -3) == 1  




             


        