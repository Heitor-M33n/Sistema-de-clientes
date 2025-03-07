import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de clientes')
app.geometry('1280x720')
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

def encontrar_filial()-> int:
    dialog = ctk.CTkInputDialog(text='Insira o número da Filial',title='Encontrar Filial')
    x = dialog.get_input()
    return x

def remove_filial():
    dialog = ctk.CTkInputDialog(text='Insira o número da Filial',title='Remover Filial')
    number = dialog.get_input()

def adi_filial():
    dialog = ctk.CTkInputDialog(text='Insira o nome da Filial',title='Adicionar Filial')
    nome = dialog.get_input()

def re_filial():
    x = encontrar_filial()
    if int(x) > 0:
        dialog = ctk.CTkInputDialog(text='Insira o novo nome da Filial',title='Renomear Filial')
        rename = dialog.get_input()

def remove_cliente():
    dialog = ctk.CTkInputDialog(text='Insira o número do Cliente',title='Remover Cliente')
    index = dialog.get_input()

def f_cliente():
    dialog = ctk.CTkInputDialog(text='Digite o id do Cliente que será removido, digite 0 caso não tenha o id do Cliente',title='Remover Cliente')
    index = dialog.get_input()

def remove_produto():
    dialog = ctk.CTkInputDialog(text='Insira o número do produto',title='Remover produto')
    index = dialog.get_input()

def adi_cliente():
    add = ctk.CTkToplevel(app)
    add.columnconfigure(0,weight=1)
    add.rowconfigure(0,weight=1)
    add.title('Adicionar Cliente')
    add.attributes("-topmost", True)
    add.grab_set()
    
    def confirmar():
        dados = []
        dados.append(nome.get())
        dados.append(cpf.get())
        dados.append(tel.get()) #.get pega o que foi inserido no entry
        
        add.destroy() #fecha a janela ao final da função
    
    pack = ctk.CTkFrame(add)
    pack.grid(row=0,column=0,pady = 10, padx= 10, sticky ='nswe')
    pack.configure(fg_color='transparent')
    
    lnome = ctk.CTkLabel(pack,text='Insira o nome do Cliente:')
    lnome.grid(row=0, column= 0, sticky = 'ew', padx=10, pady=(10, 0))

    nome = ctk.CTkEntry(pack,placeholder_text='Ex: José da Silva')
    nome.grid(row=0, column= 1, sticky = 'ew',padx=10, pady=(10, 0))

    lcpf = ctk.CTkLabel(pack,text='Insira o CPF do Cliente:')
    lcpf.grid(row=1, column= 0, sticky = 'ew',padx=10, pady=(10, 0))

    cpf = ctk.CTkEntry(pack,placeholder_text='Ex: XXX.XXX.XXX-XX')
    cpf.grid(row=1, column= 1, sticky = 'ew',padx=10, pady=(10, 0))

    ltel = ctk.CTkLabel(pack,text='Insira o telefone do Cliente:')
    ltel.grid(row=2, column= 0, sticky = 'ew',padx=10, pady=(10, 0))

    tel = ctk.CTkEntry(pack,placeholder_text='XX XXXXX-XXXX')
    tel.grid(row=2, column= 1, sticky = 'ew', padx=10, pady=(10, 0))

    ok = ctk.CTkButton(add,text='Confirmar', command=confirmar)
    ok.grid(row=3, column= 0, sticky = 'ew', padx=10, pady=10)



textbox = ctk.CTkTextbox(app, corner_radius=6,width=510)
textbox.configure(state='disable', text_color='white')
textbox.grid(row=0,column=1, pady = 10, padx= 10, sticky ='nswe')

textbox2 = ctk.CTkTextbox(app, corner_radius=6,width=510)
textbox2.configure(state='disable',text_color='white')
textbox2.grid(row=0,column=2, pady = 10, padx= (0,10), sticky ='nswe')

pack = ctk.CTkScrollableFrame(app)
pack.grid(row=0, column=0, padx=(10,0), pady=(10, 0), sticky="nsw")
pack.configure(fg_color="transparent")


title = ctk.CTkLabel(pack, text='Clientes', fg_color="gray30", corner_radius=6)
title.grid(row=0, column= 0, sticky = 'ew')

title2 = ctk.CTkLabel(pack, text='Filiais', fg_color="gray30", corner_radius=6)
title2.grid(row=6, column= 0, sticky = 'ew',pady= (10,0))

title3 = ctk.CTkLabel(pack, text='Estoques', fg_color="gray30", corner_radius=6)
title3.grid(row=10, column= 0, sticky = 'ew',pady= (10,0))

title4 = ctk.CTkLabel(pack, text='Visualização', fg_color="gray30", corner_radius=6)
title4.grid(row=14, column= 0, sticky = 'ew', pady= (10,0))

add_cliente = ctk.CTkButton(pack,text='Adicionar cliente',command= adi_cliente)
add_cliente.grid(row=1,column=0, pady= (10,0),sticky = 'ew')

del_cliente = ctk.CTkButton(pack,text='Remover cliente',command=remove_cliente)
del_cliente.grid(row=2,column=0, pady= (10,0),sticky = 'ew')

find_cliente = ctk.CTkButton(pack,text='Encontrar cliente',command=f_cliente)
find_cliente.grid(row=3,column=0, pady= (10,0),sticky = 'ew')

dados_cliente = ctk.CTkButton(pack,text='Alterar dados do cliente',command='')
dados_cliente.grid(row=4,column=0, pady= (10,0),sticky = 'ew')

novo_dado = ctk.CTkButton(pack,text='Novo tipo de dado',command='')
novo_dado.grid(row=5,column=0, pady= (10,0),sticky = 'ew')

add_filial = ctk.CTkButton(pack,text='Adicionar Filial',command=adi_filial)
add_filial.grid(row=7,column=0, pady= (10,0),sticky = 'ew')

del_filial = ctk.CTkButton(pack,text='Remover Filial',command=remove_filial)
del_filial.grid(row=8,column=0, pady= (10,0),sticky = 'ew')

rename_filial = ctk.CTkButton(pack,text='Renomear Filial',command=re_filial)
rename_filial.grid(row=9,column=0, pady= (10,0),sticky = 'ew')

cad_produto = ctk.CTkButton(pack,text='Cadastrar produto',command='')
cad_produto.grid(row=11,column=0, pady= (10,0),sticky = 'ew')

del_produto = ctk.CTkButton(pack,text='Remover produto',command=remove_produto)
del_produto.grid(row=12,column=0, pady= (10,0),sticky = 'ew')

edit_produto = ctk.CTkButton(pack,text='Alterar quantidade do produto',command='')
edit_produto.grid(row=13,column=0, pady= (10,0),sticky = 'ew')

vs_dados = ctk.CTkButton(pack,text='Visualizar Dados',command='')
vs_dados.grid(row=15,column=0, pady= (10,0),sticky = 'ew')

app.mainloop()