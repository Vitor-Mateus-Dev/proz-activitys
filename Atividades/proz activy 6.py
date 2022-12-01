Rodas = float(input('Rodas'))
Pesokg = float(input('Peso '))
Pessoas = float(input ('Pessoas no veiculo'))
if Rodas<=3 :
   print ('O veiculo designado é o tipo A ')
elif Rodas==4 and Pessoas<=8 and Pesokg<=3500:
    print ('O veiculo designado é o tipo B ')
elif Rodas>=4 and Pesokg>=3500<=6000:
    print ('O veiculo designado é o tipo C ')
elif Rodas>=4 and Pessoas>8:
    print ('O veiculo designado é o tipo D ')
elif Rodas>=4 and Pesokg>6000:
    print ('O veiculo designado é o tipo D ')
