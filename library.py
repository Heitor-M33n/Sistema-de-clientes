import os, csv, time
import library_clientes_e_filiais as cf
import library_estoque_e_vendas as ev

valores = ['id do cliente', 'nome completo', 'telefone', 'cpf'] #todos os dados são do tipo str ou int, exceto compras -> list[str], com a informação sobre a compra e seu horário ( usar datetime ) 
type_valores = ['int', 'str', 'int', 'int']
produtos_e_valores = [[], []]

def comandos_p1():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/help - Mostra os comandos') #done
    print('/sair - Fecha o sistema') #done
    print('/vis_dados - Mostra todos os dados de clientes') #done
    print('/vis_dados_filial - Mostra os dados de uma filial de escolha') #done
    print('/add_filial - Cria uma filial vazia ( e um estoque para ela )') #melhorar e consertar
    print('/del_filial - Remove uma filial, deletando seus dados ou os movendo') #done
    print('/rename_filial - Renomeia uma filial de escolha') #done
    print("  1/2 digite '/' e número da página que deseja acessar ( como /2 )")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def comandos_p2():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/add_cliente - Adiciona cliente(s) à filial de escolha') #testar
    print('/del_cliente - Remove cliente(s) de uma filial') #testar
    print('/find_cliente - Localiza cliente e seus dados por alguma informação dele.')
    print('/alterar_dados - Altera dados de escolha de um cliente')
    print('/list_filiais - Mostra todas as filiais existentes') #done
    print("  2/2 ( digite / e número da página que deseja acessar ( como /1 )")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def main_loop():
    while True:
        info = get_info()
        clientes, filiais, estoque, valores = info
        print(info)

        inp = (input('\n').strip()).lower()
        print()
        
        if inp == '/help' or inp == '/1': #done
            comandos_p1()
        elif inp == '/2': #done
            comandos_p2()
        elif inp == '/sair': #done
            print('Saindo do sistema...')
            return
        elif inp == '/vis_dados': #done
            cf.visualizar_dados(clientes, valores, filiais)
        elif inp == '/vis_dados_filial': #done
            cf.visualizar_dados_filial(clientes, valores, filiais)
        elif inp == '/add_filial': #melhorar e consertar
            cf.adicionar_filial(clientes, filiais)
        elif inp == '/del_filial': #done
            cf.remover_filial(clientes, filiais)
        elif inp == '/rename_filial': #done
            cf.rename_filial(clientes, filiais)
        elif inp == '/add_cliente': #testar
            cf.adicionar_cliente(clientes, valores, filiais, type_valores)
        elif inp == '/del_cliente': #testar
            cf.remover_cliente(clientes)
        elif inp == '/find_cliente':
            cf.encontrar_cliente()
        elif inp == '/alterar_dados':
            cf.alterar_dados_cliente()
        elif inp == '/list_filiais': #done
            print([x[0:-4] for x in filiais])
        elif inp == '/novo_tipo_de_dado':
            cf.novo_dado()
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

    return string_new

def escrever_csv(clientes: list[list[list]], filiais: list[str], modo: str='w', valores: list=0): #done
        if modo == 'w':
            for i in filiais:
                with open(f'filiais/{i}', mode='w', newline='') as file:
                    csv.writer(file).writerows(clientes[filiais.index(i)])
        elif modo == 'nova-filial':
            with open(f'filiais/{filiais[-1]}', mode='w', newline='') as file:
                return
        elif modo == 'novo-estoque':
            with open(f'estoque/estoque_{filiais[-1]}', mode='w', newline='') as file:
                return
        elif modo == 'valores':
            with open('valores.csv', mode='w', newline='') as file: