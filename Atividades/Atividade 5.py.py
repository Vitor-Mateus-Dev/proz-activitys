nome = str(input('nome'))
faltas = float(input('faltas'))
nota1 = float(input ('primeira nota'))
nota2 = float(input ('segunda'))
média = ((nota1 + nota2) /2)
if faltas > 3:
    print (' {} você  foi reprovado por faltas' .format(nome) )
elif  média >= 7:
    print ('párabens {} você foi aprovado com a média {}  ' .format(nome,média))
else:
    print (' {} você foi reprovado pela nota'  .format(nome))

   