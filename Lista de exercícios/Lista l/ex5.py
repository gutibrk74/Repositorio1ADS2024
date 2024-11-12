p = float(input('Informe o preço da mercadoria: '))
d = float(input('Informe o desconto: '))
r = p - p * d / 100

print(f'O novo preço da Mercadoria é: R${r:.2f}')
