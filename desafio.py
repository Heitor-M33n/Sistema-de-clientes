import os
estoque = []

def mostrar_estoque_ind(estoque):
    print("Estoque atual:")
    if not estoque:
        print("Não existem produtos cadastrados!")
    for produto in estoque:
        print(f"Produto: {produto["nome"]}, Quantidades: {produto["Quantidades"]}")
    

def cadastrar_produto(estoque):
    print("Cadastrar novo produto:")

    nome_produto = input("Digite o nome do produto: ")
    quantidades = []

    armazens = int(input("Digite a quantidade de armazens: "))

    for i in range(armazens):
        quantidade = int(input(f"Digite a quantidade do produto {nome_produto} no armazem {i}: "))
        quantidades.append(quantidade)

    produto = {"Nome": nome_produto, "quantidade": quantidades}
    estoque.append(produto)

    print(f"Produto {nome_produto} cadastrado com sucesso.")

def editar_quantidade(estoque):
    produto_nome = input("Digite o nome do produto: ")

    produto_encontrado = False
    for produto in estoque:
        if produto["Nome"].lower() == produto_nome.lower():
            armazem = int(input("Digite o id do armazem: "))
            nova_quantidade = int(input("Digite a nova quantidade: "))
        
            if 0 <= armazem < len(produto["quantidades"]):
                produto["quantidade"][armazem] = nova_quantidade
                print(f"Quantidade do Produto '{produto_nome}' no Armazém {armazem} atualizada para {nova_quantidade}.")
                produto = True
                break
            else:
                print("Índice do armazém inválido!")
                produto_encontrado = True
                break
    if not produto_encontrado:
        print(f"Produto '{produto_nome}' não encontrado!")

def remover_produto(estoque):
    print("Remover Produto:")
    nome_produto = input("Digite o nome do produto para ser removido: ")

    produto_encontrado = False
    for produto in estoque:
        if produto["Nome"].lower() == produto_encontrado.lower():
            estoque.remove(produto)
            print(f"Produto '{nome_produto}' removido com sucesso!")
            produto_encontrado = True
            break

    if not produto_encontrado:
        print(f"Produto '{nome_produto}' não encontrado!")

def menu():
    print("Sistema de Controle de Estoque")
    print("1. Exibir Estoque")
    print("2. Cadastrar Produto")
    print("3. Editar Quantidade")
    print("4. Remover Produto")
    print("5. Pesquisar Produto por Armazém")
    print("6. Sair")
    return int(input("Escolha uma opção: "))

while True:
    opcao = menu()
    if opcao == 1:
        mostrar_estoque(estoque)
    elif opcao == 2:
        cadastrar_produto(estoque)
    elif opcao == 3:
        editar_quantidade(estoque)
    elif opcao == 4:
        remover_produto(estoque)
    elif opcao == 6:
        print("Saindo do sistema...")
        break
    else:
        print("Por favor digitar opção valida!")
