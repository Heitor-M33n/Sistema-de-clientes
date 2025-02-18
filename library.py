import csv, os, time
import datetime as dt

'''
Sobre a matriz tridimensional:

[ > primeira dimensão: cada filial
    [ > matriz para a filial
        [
        [1], ['Heitor Ferreira Da Silva'], [84999673539], [12742580492], [[], [], []]
        ]
    ],

    [
        [
        [2], ['Cauã'], [84999673538], [12742580491], []
        ]
    ]


Sobre o csv:

Ao final de cada função, usar o escrever_csv para atualizar o .csv, ver os modos.
A cada iteração do main loop o código já atualiza a matriz automaticamente, para estarem sempre sincronizados, 
o csv com a matriz( lembrar de colocar ela quando chamar a função no main, por meio dos args da função )
'''

#modos do escrever_csv(dados, filial, modo):
# 'w' parar reescrever, só usar matrizes nele, reescreve todo o .csv, apagando o que estava nele antes, para remover ou alterar valores, sempre usar ela, reescrevendo A MATRIZ INTEIRA para evitar perca de dados
# 'a1' para append, só usar listas simples nele, adiciona uma linha ao final ( usar na adicionar clientes e funções similares, pq adiciona ao final do código )
# 'a+' para append, só usar matrizes nele, adiciona x linhas ao final ( não sei se vamos precisar, mas deixei caso houvesse necessidade )

def comandos_p1():
    print('/h - Mostra os comandos')
    print('/sair - Fecha o sistema')
    print('/visualizar_dados - Mostra todos os dados de todas as filiais')
    print('/visualizar_dados_filial - Mostra os dados de uma filial')
    print('/adicionar_cliente - Adiciona um ou mais clientes em determinada filial de escolha.')
    print('/remover_cliente - Remove um cliente pelo seu id')
    print()
    #mais...

def escrever_csv(dados: list, filial: str='Filial01', modo: str='w',):
    if modo == 'w':
        with open(f'{filial}.csv', mode='w', newline='') as file:
            csv.writer(file).writerows(dados)
            return
        
    with open(f'{filial}.csv', mode='w', newline='') as file:
        wr = csv.writer(file)
        if modo == 'a1':
            wr.writerow(dados)
        elif modo == 'a+':
            wr.writerows(dados)

def get_info() -> list[list]:
    info = []
    filiais = []
    dados = []

    dir = os.listdir()
    for arq in dir:
        if arq[-4:] == '.csv':
            filiais.append(arq)

    filiais.sort()
    info.append(filiais)

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

    info.append(dados)
    return info

def nao_esta_vazio(x):
    if not x:
        print('Função Indisponível!\n')
        return x
    else:
        return True

def remover_caracteres(string: str) -> int:
    string_numerica = ''

    for i in string:
        if i.isnumeric():
            string_numerica += i
    
    return string_numerica

def print_em_ordem_numerado(x: list, mensagem: str=' '):
    for i in range(len(x)):
        print(f'{i +1}.{mensagem}{x[i]}')

def visualizar_dados(d: list, v: list[str], f: list[str]): #de modo cru, está concluída
    v.insert(0, 'filial')
    print(v)

    for i in f: #i = filial (str)
        for y in d[f.index(i)]: #y = linha da filial (list)
            y.insert(0, i[0:-4])
            print(y)

def visualizar_dados_filial(d: list, v: list[str], f: list[str]): #de modo cru, está concluída
    f_sem_csv = [x[0:-4] for x in f]
    print_em_ordem_numerado(f_sem_csv)
    
    try:
        num = int(input('\nEscolha uma filial pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return

    if num > len(d):
        print('Filial inexistente')
        return
    
    print(v)
    for i in d[num - 1]:
        print(i)

def adicionar_cliente(dados) -> list: #em andamento
    dados_cliente = []

    dados_cliente.append(int('01003'))
    dados_cliente.append((input('Insira o nome do Cliente: ').strip()).capitalize())
    cel = input('Insira o número de telefone: ').strip()
    cpf = input('Insira o número do CPF: ').strip()

    cel_p1 = str(remover_caracteres(cel))
    cpf_p1 = str(remover_caracteres(cpf))

    if len(cel_p1) != 11 or len(cpf_p1) != 11:
        print('Dados inválidos!')
        return []

    dados_cliente.append(f'({cel_p1[0:2]}) {cel_p1[2:7]}-{cel_p1[7:]}')
    dados_cliente.append(f'{cpf_p1[0:3]}.{cpf_p1[3:6]}.{cpf_p1[6:9]}-{cpf_p1[9:]}')

    escrever_csv(dados_cliente, 'a')

def remover_cliente(dados: list) -> list:
    pass

def adicionar_filial():
    pass

def remover_filial():
    pass

def modificar_filial():
    pass

def modificar_cliente():
    pass

def encontrar_cliente():
    pass
