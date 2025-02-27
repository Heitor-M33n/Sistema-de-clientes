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
        print('Filial inexistente')
        return -1
    
    return (num - 1)

def visualizar_dados(c: list[list[list]], v: list[str], f: list[str]):
    v.insert(0, 'filial')
    print(v)

    for i in f: #i = filial (str)
        if not c[f.index(i)]:
            print([f'(vazia) {i}'])
        for y in c[f.index(i)]: #y = linha da filial i
            y.insert(0, i)
            print(y)

    v.pop(0)

def visualizar_dados_filial(c: list[list[list]], v: list[str], f: list[str]):
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
    return f

def remover_filial(c: list[list[list]], f: list[str]):
    index_filial = escolha_filial(c, f, 'para remover')

    if index_filial < 0:
        return
    
    os.remove(f'filiais/{f[index_filial]}')
    os.remove(f'estoque/estoque_{f[index_filial]}')

def rename_filial(c: list[list[list]], f: list[str]):
    index_filial = escolha_filial(c, f, 'para renomear')

    if index_filial < 0:
        return
    
    nome = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"
  
    os.rename(f'filiais/{f[index_filial]}', f'filiais/{nome}')
    os.rename(f'estoque/estoque_{f[index_filial]}', f'estoque/estoque_{nome}')

def adicionar_cliente(c: list[list[list]], v: list[str] , f: list[str], tv: list[str]):
    dados_cliente = [next_id(c)]
   
    index_filial = escolha_filial(c, f, 'para adicionar um cliente')
    
    for i in v[1:]:
        tipo = tv[v.index(i)]
        if tipo == 'str':
            x = (input(f'Insira o {i} do cliente: ').strip()).capitalize()
        elif tipo == 'int':
            x = int(l.remover_caracteres(input(f'Insira o {i} do cliente: ').strip()))
        elif tipo == 'float':
            x = int(l.remover_caracteres(input(f'Insira o {i} do cliente: ').strip()))
        if not x:
            print('Valor inválido, tentativa cancelada')
            return
        
        dados_cliente.append(x)
        
    c[index_filial].append(dados_cliente)
    l.escrever_csv(c, f, )

def encontrar_cliente(c: list[list[list]], f: list[str]) -> list:
    pass

def remover_cliente(c: list[list[list]], f: list[str]):
    try:
        id = int(input('Digite o id do cliente que será removido, digite 0 caso não tenha o id do cliente: ').strip())
    except ValueError:
        print('Insira um número')
        return
    
    if id == 0:
        encontrar_cliente(c, f)        
        
    encontrado = False
        
    for filial in c:
        for linha in filial:
            if int(linha[0]) == id:
                encontrado = True
                print('Cliente removido com sucesso.')
                filial.remove(linha)
                break
                    
    if not encontrado:
        print('Cliente não existente!')
        return
                    
    l.escrever_csv(c, f)
        
def alterar_dados_cliente(c: list[list[list]], f: list[str], vt: list): #vt[0]: tipos_de_dados, vt[1]: type_dados
    try:
        id = int(input('Digite o id do cliente que deseja alterar, digite 0 caso não tenha o id do cliente: ').strip())
    except ValueError:
        print('Insira um númer')
        return
    
    if id <= 0:
        encontrar_cliente(c, f)
        return        
        
    encontrado = False
        
    for filial in c:
        for linha in filial:
            if int(linha[0]) == id:
                encontrado = True
                print('Cliente encontrado com sucesso.')
                
                for i, campo in enumerate(vt[1]):
                    tipo = vt[0][i]
                    valor_atual = linha[i + 1]

                    entrada = input(f'Digite o novo {campo}: ').strip()

                    if tipo == 'int':
                        if entrada:
                            try:
                                linha[i + 1] = int(entrada)
                            except ValueError:
                                print(f'Valor invalido para {campo}. Deve ser um numero inteiro.')
                                return
                                
                    elif tipo == 'str':
                        linha[i + 1] = entrada if entrada else valor_atual

                    elif tipo == 'float':
                        if entrada:
                            try:
                                linha[i + 1] = str(entrada)
                            except ValueError:
                                print(f'Valor invalido para {campo}')
                                return
                    else:
                        print(f'Tipo de dado desconhecido para {campo}.')
                        return
                    
        print('Dados do cliente alterados com sucesso!') 
        break

    if not encontrado:
        print('Cliente não existente!')
        return
                    
    l.escrever_csv(c, f)

def novo_dado(c: list[list[list]], vt: list): #vt[0]: tipos_de_dados, vt[1]: type_dados
    nome_dado = (input('Insira o nome do novo tipo de dado: ').strip()).capitalize()

    escolha = input(f'Insira o número correspondente ao novo tipo de dado: ').strip()
    
    if escolha not in ['1', '2', '3']:
        print('Tipo de dado inexistente.')
        return
    
    [vt[0]].append(nome_dado)

    if escolha == '1':
        [vt[1]].append('int')
    elif escolha == '2':
        [vt[1]].append('str')
    else:
        [vt[1]].append('float')

    for filial in c:
        for linha in filial:
            linha.append('')
            
def delete_novo_daddo(c: list[list[list]], vt: list): #id, nome, tel, cpf, 
    l.print_em_ordem_numerado(vt[0][4:])
    print(len(vt[0][4:]))
    try:
        escolha = int(input(f'Insira o número correspondente ao tipo de dado a ser deletado: ').strip())
    except ValueError:
        print('Insira um número!')
        return
    
    if escolha not in range(len(vt[0][4:])):
        print('Tipo de dado inexistente')
        return
    
    index = escolha + 4
    
    
    for filial in c:
        for linha in filial:
            linha.pop(index)