import library as l
import os

'''
Sobre a matriz tridimensional:
matriz > filial > dados do cliente
[
    [ > matriz para a filial 1
        [1, 'Heitor Ferreira Da Silva', 84999673539, 13241234651, []]
    ],

    [ > matriz para a filial 2
        [2, 'Cauã', 84999673538, 112341234131, []]
        [3, 'Joaquim', 849996123358, 1132412352, []]
    ]
]

Sobre o csv: Ao final de cada função, usar o l.escrever_csv para atualizar o .csv, ver os modos.
A cada iteração do main loop o código já atualiza a matriz automaticamente, para estarem sempre sincronizados o csv e a matriz
'''

def next_id(c: list[list]) -> int:
    next_id = 1

    for filial in c:
        for linha in filial:
            if int(linha[0]) >= next_id:
                next_id = int(linha[0]) + 1
    
    return next_id

def escolha_filial(c: list[list[list[str]]], f: list[str], m: str='para visualizar seus dados') -> int:
    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
    
    try:
        num = int(input(f'\nEscolha uma filial pelo número, {m}: ').strip())
    except ValueError:
        print('Insira um número.')
        return -1

    if num > len(c) or num < 1:
        print('Filial inexistente.')
        return -1
    
    return (num - 1)

def visualizar_dados(c: list[list[list]], v: list[str], f: list[str]):
    if not c:
        print('Sistema vazio...')
        return

    v.insert(0, 'Filial')
    print(v)
    v.pop(0)

    f = [x[:-4] for x in f]

    for i in f: #filial (str)
        if not c[f.index(i)]:
            print([f'(vazia) {i}'])
        for y in c[f.index(i)]: #y = linha da filial i
            y.insert(0, i)
            print(y)

def visualizar_dados_filial(c: list[list[list]], v: list[str], f: list[str]):
    if not c:
        print('Sistema vazio...')
        return

    index_filial = escolha_filial(c, f)
    
    if index_filial < 0:
        return
    
    if not c[index_filial]:
        print('Filial vazia.')
        return

    print(v)
    for i in c[index_filial]:
        print(i)

def adicionar_filial(c: list[list[list]], f: list[str]) -> list[str]:
    filial = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"

    if filial in f:
        print('Filial já existente')
        return f
    
    if '/' in filial:
        print('Caractere inválido')
        return 
    
    f.append(filial)
    l.escrever_csv(c, f, 'nova-filial')
    l.escrever_csv(c, f, 'novo-estoque')
    print('Filial adicionada com sucesso.')
    return f

def remover_filial(c: list[list[list]], f: list[str]):
    if not f:
        print('Sistema vazio...')
        return
    
    index_filial = escolha_filial(c, f, 'para remover')

    if index_filial < 0:
        return
    
    os.remove(f'filiais/{f[index_filial]}')
    os.remove(f'estoque/estoque_{f[index_filial]}')
    print('Filial removida com sucesso.')

def rename_filial(c: list[list[list]], f: list[str]):
    if not f:
        print('Sistema vazio...')
        return

    index_filial = escolha_filial(c, f, 'para renomear')

    if index_filial < 0:
        return
    
    nome = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"
  
    os.rename(f'filiais/{f[index_filial]}', f'filiais/{nome}')
    os.rename(f'estoque/estoque_{f[index_filial]}', f'estoque/estoque_{nome}')
    print('Nome da filial alterado com sucesso.')

def adicionar_cliente(c: list[list[list]], v: list[str], f: list[str], tv: list[str]):
    dados_cliente = [next_id(c)]
   
    if not f:
        print('Não existem filiais para adicionar o cliente.')
        return

    index_filial = escolha_filial(c, f, 'para adicionar um cliente')
    
    if index_filial < 0:
        print('Ação cancelada')
        return

    for i in v[1:]:
        tipo = tv[v.index(i)]
        if tipo == 'str':
            x = (input(f'Insira o {i} do cliente: ').strip()).capitalize()
        elif tipo == 'int' or tipo == 'float':
            x = l.remover_caracteres(input(f'Insira o {i} do cliente: ').strip())
        
        if not x:
            print('Ação cancelada, dados inválidos.')
            return
        
        dados_cliente.append(x)
        
    c[index_filial].append(dados_cliente)
    l.escrever_csv(c, f)
    print('Cliente adicionado com sucesso.')

def encontrar_cliente(c: list[list[list]], f: list[str], v: list[str], modo: str = 'none') -> int:
    if not c:
        print('Sistema vazio...')
        return

    info = input('Digite alguma informação sobre o cliente: ').strip()
    tipo = (input("Essa informação é texto ou número? ( escolha entre 'txt' ou 'num' ): ").strip()).lower()

    if tipo == 'txt':
        info = info.capitalize()
    elif tipo == 'num':
        info = l.remover_caracteres(info)
    else:
        print('Tipo de informação inválido')
        return 0

    encontrado = False
    f = [x[:-4] for x in f]
    v.insert(0, 'Filial')
    dados = [v]

    print('Cliente(s) encontrado(s):\n')

    for filial in c:
        for linha in filial:
            for z in linha[1:]:
                if z == info:
                    if not encontrado:
                        encontrado = True
                        print(v)
                        v.pop(0)
                    linha.insert(0, f[c.index(filial)])
                    dados.append(linha)
                    print(linha)
                    linha.pop(0)

    if not encontrado:
        print('Nenhum')
        return 0
    elif len(dados) > 2 and modo == 'buscando id':
        try:
            return int(input('Digite o id de um dos clientes encontrados: ').strip())
        except ValueError:
            return 0
    else:
        return int(dados[1][0])
        
def remover_cliente(c: list[list[list]], f: list[str], v: list[str]):
    if not c:
        print('Sistema vazio...')
        return
    
    try:
        id = int(input('Digite o id do cliente que será removido, digite 0 caso não tenha o id do cliente: ').strip())
    except ValueError:
        print('Insira um número')
        return
    
    if not id:
        id = encontrar_cliente(c, f, v, 'buscando id')

    if id <= 0:
        print('\nAção cancelada.')
        return
    
    for filial in c:
        for linha in filial:
            if int(linha[0]) == id:
                print('Cliente removido com sucesso.')
                filial.remove(linha)
                l.escrever_csv(c, f)
                return

    print('Cliente não existente!')

def loop_alterar(c: list[list[list]], f: list[str], v: list[str], tv: list[str], cliente: list[str]):
    l.print_em_ordem_numerado(v[1:])

    try:
        index = int(input('Digite o número do valor que será alterado: ').strip())
    except ValueError:
        print('Digite um número')
        return
    
    if index not in range(len(v[1:]) + 1) or index < 1:
        print('Valor inexistente.')
        return

    if tv[index] == 'str':
        cliente[index] = (input('Digite o novo valor: ').strip()).capitalize()
    else:
        content = l.remover_caracteres(input('Digite o novo valor: ').strip())
        if content:
            cliente[index] = content

    l.escrever_csv(c, f)

def alterar_dados_cliente(c: list[list[list]], f: list[str], v: list[str], tv: list[str]):
    if not c:
        print('Sistema vazio...')
        return

    try:
        id = int(input('Digite o id do cliente que terá algum dado alterado, digite 0 caso não tenha o id do cliente: ').strip())
    except ValueError:
        print('Insira um número')
        return
    
    if not id:
        id = encontrar_cliente(c, f, v, 'buscando id')

    if id <= 0:
        print('\nAção cancelada.')
        return 
        
    encontrado = False
        
    for filial in c:
        for linha in filial:
            if int(linha[0]) == id:
                encontrado = True
                break
    
    if not encontrado:
        print('Cliente não encontrado')
        return
    
    print(v)
    print(linha)
    repetir = 'y'
    while repetir == 'y':
        loop_alterar(c, f, v, tv, linha)
        print(v)
        print(linha)
        repetir = (input('Deseja alterar outro valor do mesmo cliente? (y/n): ').strip()).lower()
    
    print('Ação cancelada.')

def novo_dado(c: list[list[list]], f: list[list[list[str]]], v: list[str], tv: list[str]):
    nome = (input('Insira o nome do novo tipo de dado: ').strip()).capitalize()
    print()

    if nome in v:
        print('Tipo de dado já existente.')
        return

    l.print_em_ordem_numerado(['texto', 'número'])
    escolha = input(f'\nInsira o número correspondente ao novo tipo de dado\n( dados de tipo numérico não aceitam caracteres alfabéticos, apenas números,\ntoda e qualquer letra inserida nesse tipo de dado será excluída. ): ').strip()
    print()

    if escolha == '1':
        tv.append('str')
    elif escolha == '2':
        tv.append('int')
    else:
        print('Tipo de dado inexistente.')
        return

    print('Nenhum cliente possui informações para esse novo tipo de dado, deseja escolher um valor padrão? (y/n)\nCaso não escolha, o valor padrão será "Desconhecido" para valores do tipo texto, e "0" para valores de tipo numérico:')
    x = (input('').strip()).lower()

    if x == 'y' and tv[-1] == 'str':
        valor_default = (input('Valor padrão: ').strip()).capitalize()
    elif x == 'y':
        valor_default = l.remover_caracteres(input(f'Valor padrão: ').strip())
    elif tv[-1] == 'str':
        valor_default = 'Desconhecido'
    else:
        valor_default = '0'

    print('Valor padrão definido e adicionado com sucesso.')

    for filial in c:
        for linha in filial:
            linha.append(valor_default)

    v.append(nome)
    vt = [v, tv]
    l.escrever_csv(vt, f, 'valores')
    l.escrever_csv(c, f)
            
def remover_dado(c: list[list[list]], f: list[str], v: list[str], tv: list[str]):
    l.print_em_ordem_numerado(v[2:])

    try:
        escolha = int(input(f'Insira o número correspondente ao tipo de dado a ser deletado: ').strip())
    except ValueError:
        print('Insira um número!')
        return
    
    if escolha not in range(len(v[2:]) + 1) or escolha < 1:
        print('Tipo de dado inexistente')
        return
    
    index = escolha + 1
    v.pop(index)
    tv.pop(index)
    vt = [v, tv]
    
    for filial in c:
        for linha in filial:
            linha.pop(index)

    print('Dado removido com sucesso.')
    l.escrever_csv(vt, f, 'valores')
    l.escrever_csv(c, f)