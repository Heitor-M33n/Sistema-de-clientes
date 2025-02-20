import csv, os, time
import library as l

#To-Do:
#Modularizar a escolha de filial
#implementar o l.next_id() antes das funções de cliente
#funções referentes aos clientes ( TODAS )

def comandos_p1():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/help - Mostra os comandos') #done
    print('/sair - Fecha o sistema') #done
    print('/vis_dados - Mostra todos os dados ') #done ( modo simples )
    print('/vis_dados_filial - Mostra os dados de uma filial de escolha') #done ( modo simples )
    print('/add_filial - Cria uma filial vazia ') #modificar
    print('/del_filial - Remove uma filial, deletando seus dados ou os movendo') #done
    print('/rename_filial - Renomeia uma filial de escolha') #done
    print('  1/2 ( digite o / e número da página que deseja acessar, como /2 )')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def comandos_p2():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/find_cliente - Localiza cliente e seus dados por alguma informação dele.')
    print('/add_cliente - Adiciona cliente(s) a filial de escolha')
    print('/del_cliente - Remove cliente(s) de uma filial')
    print('/alterar_dados - Altera dados de escolha de um cliente')
    print('/list_filiais - Mostra todas as filiais existentes')
    print('  2/2 ( digite / e número da página que deseja acessar, como /1 )')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def escrever_csv_w(dados: list[list[list]], filiais: list[str], modo: str='w'): #completa
        if modo == 'w':
            for i in filiais:
                with open(i, mode='w', newline='') as file:
                    csv.writer(file).writerows(dados[filiais.index(i)])
        elif modo == 'nova-filial':
            with open(filiais[-1], mode='w', newline='') as file:
                csv.writer(file).writerow(list())

def visualizar_dados(d: list, v: list[str], f: list[str]): #de modo cru, está concluída
    v.insert(0, 'filial')
    print(v)

    for i in f: #i = filial (str)
        for y in d[f.index(i)]: #y = linha da filial (list)
            y.insert(0, i[0:-4])
            print(y)

    v.pop(0)

def visualizar_dados_filial(d: list, v: list[str], f: list[str]): #de modo cru, está concluída
    f_sem_csv = [x[0:-4] for x in f]
    l.print_em_ordem_numerado(f_sem_csv)
    
    try:
        num = int(input('\nEscolha uma filial pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return

    if num > len(d) or num < 1:
        print('Filial inexistente')
        return
    
    print(v)
    for i in d[num - 1]:
        print(i)

def adicionar_filial(d: list[list], f: list[str]) -> list[str]: #completa, precisa de testes
    filial = f"{(input('Insira o nome para a nova filial: ').strip()).capitalize()}.csv"

    if filial in f:
        print('Filial já existente')
        return f
    
    f.append(filial)
    d.append(list())
    escrever_csv_w(d, f, 'nova-filial')
    return f

def remover_filial(f: list[str]): #completa, falta o mover
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

def adicionar_cliente(d: list[list], v: list[str] , f: list[str], tv: list[str]):
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

    d[num - 1].append(dados_cliente)

    escrever_csv_w(d, f)

def remover_cliente(dados: list) -> list:
    l.print_em_ordem_numerado()
    
    try:
        num = int(input('\nEscolha umm dado para localizar o cli pelo número, para visualizar seus dados: ').strip())
    except ValueError:
        print('Insira um número.')
        return

def alterar_dados_cliente():
    pass