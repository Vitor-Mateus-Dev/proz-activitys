Operação = float(input(
    "digite se será soma(1), subtração(2), multiplicação(3), divisão(4)"))
Valor_inicial = int(input("digite um valor"))
Valor_secundario = int(input("digite o segundo valor"))
if Operação == (1):
    resultado_soma = Valor_inicial + Valor_secundario
    print(resultado_soma)
elif Operação == (2):
    resultado_subtração = Valor_inicial - Valor_secundario
    print(resultado_subtração)
elif Operação == (3):
    resultado_multiplicação = Valor_inicial * Valor_secundario
    print(resultado_multiplicação)
elif Operação == (4):
    resultado_divisão = Valor_inicial / Valor_secundario
    print(resultado_divisão)
