def adicionar(a,b):
    return a+b

def substrair(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    if b != 0:
        return a/b
    else:
        return 'não é possivel dividir por zero'

while True:
    op = input('selecione a operação : +, -, *, / ou sair :')
    if op == 'sair':
        break
    a = float(input('digite um numero: '))
    b = float(input('digite um numero: '))

    if op == '+':
        print('Resultado :',adicionar(a,b))
    elif op == '-':
        print('Resultado :', substrair(a, b))
    elif op == '*':
        print('Resultado :', multi(a, b))
    elif op == '/':
        print('Resultado :', divi(a, b))
    else:
        print('operação invalida')

