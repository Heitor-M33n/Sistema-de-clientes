import os, csv, time
import library_clientes_e_filiais as cf
import library_estoque_e_vendas as ev

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

valores = ['id do cliente', 'nome completo', 'telefone', 'cpf', 'compras'] #todos os dados são do tipo str ou int, exceto compras -> list[str], com a informação sobre a compra e seu horário ( usar datetime ) 
type_valores = ['int', 'str', 'int', 'int', 'list[str]']

def comandos_p1():
    time.sleep(1)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('/help - Mostra os comandos') #done
    print('/sair - Fecha o sistema') #done
    print('/vis_dados - Mostra todos os dados de clientes') #done
    print('/vis_dados_filial - Mostra os dados de uma filial de escolha') #done
    print('/add_filial - Cria uma filial vazia ') #melhorar e consertar
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
        clientes = info[0]
        filiais = info[1]
        estoque = info[2]
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
            cf.remover_filial(filiais)
        elif inp == '/rename_filial': #done
            cf.rename_filial(filiais)
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
        elif inp == '/novo_dado':
            cf.novo_dado()
        else:
            print('Opção inválida.')

def get_info() -> list[list[list[list[str]]], list[str], list[str]]:
    clientes = []
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

    return [clientes, filiais, estoque]
   
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