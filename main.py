import library as l
import time as t

tipos_de_dados = ['id do cliente', 'nome', 'telefone', 'cpf', 'compras'] #todos os dados são do tipo str ou int, exceto compras -> list[str], com a informação sobre a compra e seu horário ( usar datetime ) 

print('------------------------------------------------------------------------')
print('Bem vindo ao sistema de gerenciamento de clientes e vendas!')
t.sleep(0.75)
print("digite /help para ver os comandos disponíveis, /sair para parar o programa.") #temporariamente, /help -> h, /sair -> s
print('------------------------------------------------------------------------')
t.sleep(1.25)

while True:
    info = l.get_info()
    filiais = info[0]
    dados = info[1]

    print('( Temporário )', filiais, '+', dados) #temporário
    inp = (input('\n').strip()).lower()
    t.sleep(0.5)
    print()

    if inp == 'h' or inp == '1':
        l.comandos_p1()
    elif inp == 's':
        print('Saindo do sistema...')
        break
    elif inp == '/visualizar_dados':
        if l.nao_esta_vazio(filiais):
            l.visualizar_dados(dados, tipos_de_dados, filiais)
    elif inp == '/visualizar_dados_filial':
        if l.nao_esta_vazio(filiais):
            l.visualizar_dados_filial(dados, tipos_de_dados, filiais)
    elif inp == '/adicionar_cliente':
        l.adicionar_cliente(dados)
    elif inp == '/remover_cliente':
        if l.nao_esta_vazio(dados):
            l.remover_cliente(dados)
    else:
        print('Opção inválida.')

    #adicionar funções conforme for fazendo...
