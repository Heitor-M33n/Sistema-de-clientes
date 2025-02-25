import os, csv

'''
Sobre a matriz tridimensional:

[ > primeira dimensão: cada filial
    [ > matriz para a filial
        [
        [1, 'Heitor Ferreira Da Silva', 84999673539, 12742580492, []]
        ]
    ],

    [
        [
        [2, 'Cauã', 84999673538, 12742580491, []]
        ]
    ]
]

Sobre o csv: Ao final de cada função, usar o escrever_csv para atualizar o .csv, ver os modos.
A cada iteração do main loop o código já atualiza a matriz automaticamente, para estarem sempre sincronizados, 
o csv com a matriz( lembrar de colocar ela quando chamar a função no main, por meio dos args da função )
'''

def get_info() -> list[list[str], list[str]]:
    info = []
    estoques = []
    filiais = []
    dados = []

    dir = os.listdir()
    for arq in dir:
        if arq == 'filiais':
            for filial in arq:
                filiais.append(filial)
        elif arq == 'estoque':
            for estoque in arq:
                estoques.append(estoque)

    filiais.sort()

    if not filiais:
        print('Sistema vazio, algumas funções ficarão indisponíveis.')
        info.append(dados)
        return info
    
    for arq_csv in filiais:
        filial = []
        with open(arq_csv, mode='r', newline='') as file:
            for row in csv.reader(file):
                filial.append(row)
        dados.append(filial)

    vazio = True
    for i in dados:
        if i:
            vazio = False
    
    if vazio:
        print('Filial(is) vazia(s), algumas funções ficarão indisponíveis.')

    info.append(filiais)
    info.append(dados)
    info.append(estoques)
    return info

def nao_esta_vazio(x):
    if not x:
        print('Função Indisponível!\n')
        return x
    else:
        return True
   
def print_em_ordem_numerado(x: list, mensagem: str=' '):
    for i in range(len(x)):
        print(f'{i + 1}.{mensagem}{x[i]}')

def remover_caracteres(string: str, modo: str='num') -> int:
    string_new = ''

    for i in string:
        if modo == 'num':
            if i.isnumeric():
                string_new += i
        elif modo == 'whitespace':
            if not i.isspace():
                string_new += i

    return string_new