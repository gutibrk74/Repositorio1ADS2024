d = int(input('Informe os Dias: '))
h = int(input('Informe as Horas: '))
m = int(input('Informe os Minutos: '))
s = int(input('Irforme os Segundos: '))

r = d * 24 * 60 * 60 + h * 60 * 60 + m * 60 + s

print(f'O total em segundos é: {r}')
