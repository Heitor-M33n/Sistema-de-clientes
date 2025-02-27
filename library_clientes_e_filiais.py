import library as l
import os

'''
Sobre a matriz tridimensional:

[ > primeira dimensão: cada filial
    [ > matriz para a filial
        [1, 'Heitor Ferreira Da Silva', 84999673539, 13241234651, []]
    ],

    [
        [2, 'Cauã', 84999673538, 112341234131, []]
        [3, 'Joaquim', 849996123358, 1132412352, []]
    ]
]

Sobre o csv: Ao final de cada função, usar o escrever_csv para atualizar o .csv, ver os modos.
A cada iteração do main loop o código já atualiza a matriz automaticamente, para estarem sempre sincronizados, 
o csv com a matriz( lembrar de colocar ela quando chamar a função no main, por meio dos args da função )
'''

#To-Do:
#Modularizar a escolha de filial
#funções ( ver comandos )
#função do novo tipo de dado ( :sob: )

def next_id(c: list[list]) -> int: #done
    next_id = 1

    for filial in c:
        for linha in filial:
            if linha[0] >= next_id:
                next_id = linha[0] + 1
    
    return next_id

def escolha_filial(c: list[list[list[str]]], f: list[str]) -> int: #done
    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
    
    try:
        num = int(input('\nEscolha uma filial pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return -1

    if num > len(c) or num < 1:
        print('Filial inexistente')
        return -1
    
    return (num - 1)

def visualizar_dados(c: list[list[list[str]]], v: list[str], f: list[str]): #de modo cru, está concluída
    v.insert(0, 'filial')
    print(v)

    for i in f: #i = filial (str)
        if not c[f.index(i)]:
            print([f'(vazia) {i}'])
        for y in c[f.index(i)]: #y = linha da filial i
            y.insert(0, i)
            print(y)

    v.pop(0)

def visualizar_dados_filial(c: list[list[list[str]]], v: list[str], f: list[str]): #de modo cru, está concluída
    index_filial = escolha_filial(c, f)
    
    if index_filial < 0:
        return
    
    if not c[index_filial]:
        print('Filial vazia.')
        return

    print(v)
    for i in c[index_filial]:
        print(i)

def adicionar_filial(c: list[list[list[str]]], f: list[str]) -> list[str]: #done
    filial = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"

    if filial in f:
        print('Filial já existente')
        return f
    
    f.append(filial)
    l.escrever_csv(c, f, 'nova-filial')
    l.escrever_csv(c, f, 'novo-estoque')
    return f

def remover_filial(c: list[list[list[str]]], f: list[str]): #done
    index_filial = escolha_filial(c, f)

    if index_filial < 0:
        return
    
    os.remove(f'filiais/{f[index_filial]}')
    os.remove(f'estoque/estoque_{f[index_filial]}')

def rename_filial(c: list[list[list[str]]], f: list[str]): #done
    index_filial = escolha_filial(c, f)

    if index_filial < 0:
        return
    
    nome = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"
  
    os.rename(f'filiais/{f[index_filial]}', f'filiais/{nome}')
    os.rename(f'estoque/estoque_{f[index_filial]}', f'estoque/estoque_{nome}')

def encontrar_cliente():
    pass

def adicionar_cliente(c: list[list], v: list[str] , f: list[str], tv: list[str]):
    dados_cliente = [next_id(c)]

    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
   
    try:
        num = int(input('\nEscolha a filial do cliente, pelo seu número: ').strip())
    except ValueError:
        print('Insira um número.')
        return

    if num > len(f) or num < 1:
        print('Essa filial não existe.')
        return

    for i in v[1:]:
        tipo = tv[v.index(i)]
        if tipo == 'str':
            dados_cliente.append((input(f'Insira o {i} do cliente: ').strip()).capitalize())
        elif tipo == 'int':
            dados_cliente.append(int(l.remover_caracteres(input(f'Insira o {i} do cliente: ').strip())))

    c[num - 1].append(dados_cliente)

def remover_cliente() -> list:
    pass

def alterar_dados_cliente():
    pass

def novo_dado():
    pass