import library as l
import library_estoque_e_vendas as ev
import library_clientes_e_filiais as cf
import time as t

tipos_de_valor = ['id do cliente', 'nome completo', 'telefone', 'cpf', 'compras'] #todos os dados são do tipo str ou int, exceto compras -> list[str], com a informação sobre a compra e seu horário ( usar datetime ) 
type_tipos_de_valor = ['int', 'str', 'int', 'int', 'list[str]']

print('Iniciando...')
t.sleep(2)
print('============================================================')
print('Bem vindo ao sistema de controle de lojas, com funções')
print('para gestão de clientes, filiais, estoque e vendas.\n')
t.sleep(0.75)
print('Digite /cliente_e_filiais para acessar as funções referentes')
print('à modificação de dados dos clientes e filiais\n')
t.sleep(0.75)
print('Digite /estoque_e_vendas para acessar as funções referentes')
print('à modificação do estoque, visualização e cadastro de vendas')
print('===========================================================\n')

sistema = (input('').strip()).lower()

while True:
    info = l.get_info()
    filiais = info[0]
    dados = info[1]

    if sistema == '/cliente_e_filiais':
        print('---------------------------------------------------------------------------------')
        print('           Bem vindo ao sistema de gerenciamento de clientes e filiais!          ')
        print('digite /help para ver os comandos disponíveis, /s para retornar pro menu inicial.')
        print('---------------------------------------------------------------------------------')
        cf.condicionais()
    elif sistema == '/estoque_e_vendas':
        print('---------------------------------------------------------------------------------')
        print('            Bem vindo ao sistema de gerenciamento de estoque e vendas            ')
        print('digite /help para ver os comandos disponíveis, /s para retornar pro menu inicial.')
        print('---------------------------------------------------------------------------------')
        ev.condicionais()
    elif sistema == '/sair':
        print('Saindo...')
        break
    else:
        print('-------------------')
        print('Sistema inexistente')
        print('-------------------')
        
    print('Digite /sair para fechar o programa,')
    print('ou um dos comandos para acessar as funções.\n/clientes_e_filiais; /estoque_e_vendas')
    sistema = (input().strip()).lower()
    print()
