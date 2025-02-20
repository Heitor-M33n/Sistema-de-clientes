import library as l
import library_estoque_e_vendas as ev
import library_clientes_e_filiais as cf
import time as t

tipos_de_valor = ['id do cliente', 'nome completo', 'telefone', 'cpf', 'compras'] #todos os dados são do tipo str ou int, exceto compras -> list[str], com a informação sobre a compra e seu horário ( usar datetime ) 
tipos_dos_tipos_de_valor = ['int', 'str', 'int', 'int', 'list[str]']

#To-Do
#Modularizar as condicionais do main
#Funções incompletas, as completas estão com comentário

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

#sistema = (input('').strip()).lower()
sistema = '/cliente_e_filiais' #para testes

print(sistema)

while True:
    if sistema == '/cliente_e_filiais':
        print('---------------------------------------------------------------------------------')
        print('           Bem vindo ao sistema de gerenciamento de clientes e filiais!          ')
        print('digite /help para ver os comandos disponíveis, /s para retornar pro menu inicial.')
        print('---------------------------------------------------------------------------------')
    elif sistema == '/estoque_e_vendas':
        print('---------------------------------------------------------------------------------')
        print('            Bem vindo ao sistema de gerenciamento de estoque e vendas            ')
        print('digite /help para ver os comandos disponíveis, /s para retornar pro menu inicial.') #temporariamente, /help -> h, /sair -> s
        print('---------------------------------------------------------------------------------')
    elif sistema == '/sair':
        print('Saindo...')
        break
    else:
        print('-------------------')
        print('Sistema inexistente')
        print('-------------------')

    while sistema == '/cliente_e_filiais':
        info = l.get_info()
        filiais = info[0]
        dados = info[1]

        inp = (input('\n').strip()).lower()
        t.sleep(0.5)
        print()

        if inp == '/help' or inp == '/1': #done
            cf.comandos_p1()
        elif inp == '/2': #done
            cf.comandos_p2()
        elif inp == '/sair': #done
            print('Saindo do sistema...')
            break
        elif inp == '/vis_dados': #done
            if l.nao_esta_vazio(filiais):
                cf.visualizar_dados(dados, tipos_de_valor, filiais)
        elif inp == '/vis_dados_filial': #done
            if l.nao_esta_vazio(filiais):
                cf.visualizar_dados_filial(dados, tipos_de_valor, filiais)
        elif inp == '/add_filial': #melhorar
            cf.adicionar_filial(dados, filiais)
        elif inp == '/del_filial': #done
            if l.nao_esta_vazio(filiais):
                cf.remover_filial(filiais)
        elif inp == '/rename_filial': #done
            if l.nao_esta_vazio(filiais):
                cf.rename_filial(filiais)
        elif inp == '/add_cliente':
            if l.nao_esta_vazio(filiais):
                cf.adicionar_cliente(dados, tipos_de_valor, filiais, tipos_dos_tipos_de_valor)
        elif inp == '/del_cliente':
            if l.nao_esta_vazio(dados):
                cf.remover_cliente(dados)
        elif inp == '/find_cliente':
            if l.nao_esta_vazio(dados):
                cf.encontrar_cliente
        elif inp == '/alterar_dados':
            if l.nao_esta_vazio(dados):
                cf.alterar_dados_cliente():
        elif inp == '/list_filiais': #done
            if l.nao_esta_vazio(filiais):
                print([x[0:-4] for x in filiais])
        else:
            print('Opção inválida.')

            #adicionar funções conforme for fazendo...

    while sistema == '/estoque_e_vendas':
        #ainda será implementado
        break
    print('Digite /sair para fechar o programa,')
    print('ou um dos comandos para acessar as funções.')
    sistema = (input().strip()).lower()
    print()
