import library as l
import library_estoque_e_vendas as ev
import library_clientes_e_filiais as cf
import time as t

print('Iniciando...')
t.sleep(0)
print('===============================================================')
print('Bem vindo ao sistema de controle de lojas, com funções')
print('para gestão de clientes, filiais, estoque e vendas.')
print('Digite /help para ver os comandos, /sair para fechar o sistema.')
print('===============================================================\n')

l.main_loop()
t.sleep(1)