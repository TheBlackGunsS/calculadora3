def sumar():
    a = float(input("Introduce el primer número para sumar: "))
    b = float(input("Introduce el segundo número para sumar: "))
    return a + b

def restar():
    a = float(input("Introduce el primer número para restar: "))
    b = float(input("Introduce el segundo número para restar: "))
    return a - b

def multiplicar():
    a = float(input("Introduce el primer número para multiplicar: "))
    b = float(input("Introduce el segundo número para multiplicar: "))
    return a * b

def dividir():
    a = float(input("Introduce el primer número para dividir: "))
    b = float(input("Introduce el segundo número para dividir: "))
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a/b
