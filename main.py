from datetime import datetime
from src.products import Products

# produto = Products(4, '300g', 'arroz e cassoulet',datetime.strptime('02/06/2020', '%d/%m/%Y'), 12)
# produto.create_product()

produtos: Products = Products.get_products()

# coluna apenas para ajudara na tabulação
cabecalho: list = ['Categoria', 'Descrição', 'Fabricação', 'Quantidade']
print('{:<11}{:<40}{:<15}{:<10}'.format(*cabecalho).upper())
for produto in produtos:
    print(f'{produto.category:<11}'
          f'{produto.description:<40}'
          f'{datetime.strftime(produto.manufacture_dt, "%d/%m/%Y"):<15}'
          f'{produto.qty:>10}')
