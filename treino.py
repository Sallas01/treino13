sal = float(input('qual e o seu salario? R$'))
aum = sal + (sal * 20 / 100)
fgts = aum - (aum * 11 / 100)
fund = fgts - (fgts * 15 / 100)
final = fund
print('Se você recebe {:.2f}R$ com o aumento de 20% seu salarío vai ser de {:.2f}R$. '
      '\n Mas com os descontos do FGTS ira sobrar {:.2f}R$. '
      '\n Nao se esqueca do fundo de garantia com esses descontos ira sobrar {:.2f}R$'.format(sal, aum, fgts, fund, final))

