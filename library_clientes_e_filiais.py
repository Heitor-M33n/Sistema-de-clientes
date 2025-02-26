import csv, os, time
import library as l

#To-Do:
#Modularizar a escolha de filial
#funções ( ver comandos )
#função do novo tipo de dado ( :sob: )

def next_id(c: list[list]):
    next_id = 1

    for filial in c:
        for linha in filial:
            if linha[0] >= next_id:
                next_id = linha[0] + 1

def escrever_csv_w(clientes: list[list[list]], filiais: list[str], modo: str='w'): #done
        if modo == 'w':
            for i in filiais:
                with open(f'filiais/{i}', mode='w', newline='') as file:
                    csv.writer(file).writerows(clientes[filiais.index(i)])
        elif modo == 'nova-filial':
            with open(f'filiais/{filiais[-1]}', mode='w', newline='') as file:
                return

def escolha_filial(f: list[str], c: list[list[list[str]]]) -> int: #done
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
    index_filial = escolha_filial(f, c)
    
    if index_filial < 0:
        return
    
    if not c[index_filial]:
        print('Filial vazia.')
        return

    print(v)
    for i in c[index_filial]:
        print(i)

def adicionar_filial(c: list[list[list[str]]], f: list[str]) -> list[str]:
    filial = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"

    if filial in f:
        print('Filial já existente')
        return f
    
    f.append(filial)
    escrever_csv_w(c, f, 'nova-filial')
    return f

def remover_filial(f: list[str], c: list[list]):
    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
   
    try:
        num = int(input('\nEscolha a filial pelo seu número: ').strip())
    except ValueError:
        print('Insira um número.')
        return

    if num > len(f) or num < 1:
        print('Essa filial não existe.')
        return

    os.remove(f[num - 1])

def rename_filial(f: list[str]): #completa
    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
   
    try:
        num = int(input('\nEscolha a filial para ser renomeada, pelo seu número: ').strip())
    except ValueError:
        print('Insira um número.')
        return f

    if num > len(f) or num < 1:
        print('Essa filial não existe.')
        return

    filial = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"
  
    os.rename(f[num - 1], filial)

def encontrar_cliente():
    pass

def adicionar_cliente(c: list[list], v: list[str] , f: list[str], tv: list[str]):
    dados_cliente = [10] #criação de id

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
        else:
            dados_cliente.append(list())

    c[num - 1].append(dados_cliente)

    escrever_csv_w(c, f)

def remover_cliente(dados: list) -> list:
    l.print_em_ordem_numerado()
    
    try:
        num = int(input('\nEscolha umm dado para localizar o cli pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return

def alterar_dados_cliente():
    pass

def novo_dado():
    pass