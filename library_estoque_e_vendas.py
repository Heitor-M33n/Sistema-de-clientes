import library as l
import library_clientes_e_filiais as cf

'''
[ > matriz de estoque completa
    ['produto', 'valor', 'qnt-F1', 'qnt-F2']
    ['arroz', 4,55, 123, 1135]
    ['feijao', 3,22, 124, 145]
]
'''

def cadastrar_produto(p: list[str], e: list[list]) -> list[str]:
    nome_produto = (input("Digite o nome do produto: ").strip()).capitalize()
    valor = input("Insira o preço do produto: ").strip()
    x = ''

    for i in valor:
        if i.isnumeric():
            x += i
        elif i == '.' or i == ',':
            x += '.'

    try:
        round(float(x), 2)
    except ValueError:
        print('Insira um número!')
        return

    p[0].append(nome_produto)
    p[1].append(valor)

    return p

def remover_produto(p: list[str], e: list[list]) -> list[str]:
    index_produto = escolha_produto(p, 'para remove-lo')
    p[0].pop(index_produto)
    p[1].pop(index_produto)

    return p, e

def escolha_produto(p: list[list], m: str) -> int:
    l.print_em_ordem_numerado(p)
    
    try:
        num = int(input(f'\nEscolha um produto pelo número, {m}: ').strip())
    except ValueError:
        print('Insira um número.')
        return -1

    if num > len(p) or num < 1:
        print('Estoque inexistente')
        return -1
    
    return (num)

def alterar_quantidade(e: list[list], p : list[list]):
    index_produto = escolha_produto(e, 'para alterar a quantidade')
    e_sem_csv = [x[0:-4] for x in e[3:]]
    l.print_em_ordem_numerado(e_sem_csv)
    
    try:
        num = int(input('\nEscolha um Estoque pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return -1

    if num > len(e_sem_csv) or num < 1:
        print('Estoque inexistente')
        return -1
    
    index_estoque = (num + 1)
    try:
        nova_quantidade = int(input('Insira a nova quantidade do produto: '))
    except ValueError:
        print('Insira um número')
    
    p.insert(index_produto,nova_quantidade)