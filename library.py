import os, csv, time
import library_clientes_e_filiais as cf
import library_estoque_e_vendas as ev

def comandos_p1():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/help - Mostra os comandos')
    print('/sair - Fecha o sistema')
    print('/vis_dados - Mostra todos os dados de clientes')
    print('/vis_dados_filial - Mostra os dados de uma filial de escolha')
    print('/add_filial - Cria uma filial vazia ( e um estoque para ela )')
    print('/del_filial - Remove uma filial, deletando seus dados ( e seu estoque )')
    print('/rename_filial - Renomeia uma filial de escolha')
    print('  1/3 digite / e número da página que deseja acessar ( como /2 )')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def comandos_p2():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/add_cliente - Adiciona cliente(s) à filial de escolha')
    print('/find_cliente - Localiza cliente por alguma informação dele.')
    print('/del_cliente - Remove cliente(s) de uma filial')
    print('/alterar_dados - Altera dados de escolha de um cliente')
    print('/list_filiais - Mostra todas as filiais existentes')
    print('  2/3 digite / e número da página que deseja acessar')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def comandos_p3():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('  3/3 digite / e número da página que deseja acessar')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def main_loop():
    while True:
        info = get_info()
        clientes, filiais, estoque, valores_totais = info
        tipos_de_dado, type_dados, produtos, precos = valores_totais

        inp = (input('\n').strip()).lower()
        print()
        
        if inp == '/help' or inp == '/1':
            comandos_p1()
        elif inp == '/2':
            comandos_p2()
        elif inp == '/sair':
            print('Saindo do sistema...')
            return
        elif inp == '/vis_dados':
            cf.visualizar_dados(clientes, tipos_de_dado, filiais)
        elif inp == '/vis_dados_filial':
            cf.visualizar_dados_filial(clientes, tipos_de_dado, filiais)
        elif inp == '/add_filial':
            cf.adicionar_filial(clientes, filiais)
        elif inp == '/del_filial':
            cf.remover_filial(clientes, filiais)
        elif inp == '/rename_filial':
            cf.rename_filial(clientes, filiais)
        elif inp == '/add_cliente':
            cf.adicionar_cliente(clientes, tipos_de_dado, filiais, type_dados)
        elif inp == '/del_cliente':
            cf.remover_cliente(clientes, filiais)
        elif inp == '/find_cliente':
            cf.encontrar_cliente(clientes, filiais, valores_totais)
        elif inp == '/alterar_dados_cliente':
            cf.alterar_dados_cliente(clientes, filiais)
        elif inp == '/list_filiais':
            print([x[0:-4] for x in filiais])
        elif inp == '/novo_tipo_de_dado':
            cf.novo_dado(clientes, valores_totais)
        elif inp == '/add_produto':
            produtos_e_valores = ev.cadastrar_produto(produtos_e_valores)
        else:
            print('Opção inválida.')

def get_info() -> list[list[list[list[str]]], list[str], list[str], list]:
    clientes = []; valores = []
    filiais = os.listdir('filiais')
    estoque = os.listdir('estoque')

    filiais.sort()
    estoque.sort()

    for i in filiais:
        filial = []
        with open(f'filiais/{i}', mode='r', newline='') as file:
            for linha in csv.reader(file):
                filial.append(linha)
        clientes.append(filial)
    
    with open(f'valores.csv', mode='r', newline='') as file:
        for linha in csv.reader(file):
            valores.append(linha)

    return [clientes, filiais, estoque, valores]
   
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

    string_new.strip()
    if string_new:
        return string_new
    return False

def escrever_csv(dados: list[list[list]], filiais: list[str], modo: str='w'): #done
        if modo == 'w':
            for i in filiais:
                with open(f'filiais/{i}', mode='w', newline='') as file:
                    csv.writer(file).writerows(dados[filiais.index(i)])
        elif modo == 'nova-filial':
            with open(f'filiais/{filiais[-1]}', mode='w', newline='') as file:
                return
        elif modo == 'novo-estoque':
            with open(f'estoque/estoque_{filiais[-1]}', mode='w', newline='') as file:
                return
        elif modo == 'valores':
            with open('valores.csv', mode='w', newline='') as file:
                csv.writer(file).writerows(dados)
                return
