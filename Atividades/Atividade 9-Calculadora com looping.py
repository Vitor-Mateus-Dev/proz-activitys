'''Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até
que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair
Digite o número para a operação correspondente e caso o usuário introduza qualquer outro,
 o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar
 a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.
É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.'''

sair = False
while sair == False:
 Operação = float(input(
    "digite se será soma(1), subtração(2), multiplicação(3), divisão(4) ou sair(0)"))
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
 elif Operação == (0):
    sair = True
