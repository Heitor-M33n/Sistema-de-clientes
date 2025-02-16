import library as l
import time as t

tipos_de_dados = [['id da filial'], ['id do cliente'], ['nome'], ['telefone'], ['cpf'], ['compras']]

print('------------------------------------------------------------------------')
print('Bem vindo ao sistema de gerenciamento de clientes!')
t .sleep(0.75)
print("digite h para ver os comandos disponíveis, s para parar o programa.")
print('------------------------------------------------------------------------')
t.sleep(1.25)

while True: #Esses comentários de baixo são o modo ideal de fazer, ver library
    info = l.get_info()
    filiais = info[0]
    dados = info[1]

    print(filiais, '+', dados) #para testes
    inp = (input('\n').strip()).lower(); print()

    if inp == '/h':
        l.comandos()
    elif inp == 's':
        print('Saindo do sistema...')
        break
    elif inp == '/visualizar_dados':
        if not l.is_vazio(filiais):
            l.visualizar_dados()
    elif inp == '/visualizar_dados_filial':
        if not l.is_vazio(filiais):
            l.visualizar_dados_filial(dados, filiais)
    elif inp == '/adicionar_cliente':
        l.adicionar_cliente(dados)
    elif inp == '/remover_cliente':
        if not l.is_vazio(dados):
            l.remover_cliente(dados)
    else:
        print('Opção inválida.')

    #adicionar funções conforme for fazendo...