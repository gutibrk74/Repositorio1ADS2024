m = float(input('Mercadoria: '))
d = float(input('Desconto: ')) / 100 

x = m * d
y = m - x

print('valor do desconto','R$',x)
print('Novo preço da mercadoria', 'R$',y)


