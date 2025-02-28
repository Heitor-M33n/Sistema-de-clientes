import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title('Sistema de clientes')
app.geometry('600x400')
app.columnconfigure((0,1,2), weight=1)
app.rowconfigure(0, weight=1)


pack = ctk.CTkFrame(app)
pack.grid(row=0, column=0, padx=(10,0), pady=(10, 0), sticky="nsw")
pack.configure(fg_color="transparent")

pack2 = ctk.CTkFrame(app)
pack2.grid(row=0, column=1, pady=(10, 0), sticky="nsw")
pack2.configure(fg_color="transparent")

pack3 = ctk.CTkFrame(app)
pack3.grid(row=0, column=2, padx=(0,10), pady=(10, 0), sticky="nsw")
pack3.configure(fg_color="transparent")


title = ctk.CTkLabel(pack, text='Clientes', fg_color="gray30", corner_radius=6)
title.grid(row=0, column= 0, sticky = 'ew')

title2 = ctk.CTkLabel(pack2, text='Filiais', fg_color="gray30", corner_radius=6)
title2.grid(row=0, column= 0, sticky = 'ew')

title3 = ctk.CTkLabel(pack3, text='Estoques', fg_color="gray30", corner_radius=6)
title3.grid(row=0, column= 0, sticky = 'ew')


add_cliente = ctk.CTkButton(pack,text='Adicionar cliente',command='')
add_cliente.grid(row=1,column=0, pady= (10,0),sticky = 'ew')

del_cliente = ctk.CTkButton(pack,text='Remover cliente',command='')
del_cliente.grid(row=2,column=0, pady= (10,0),sticky = 'ew')

find_cliente = ctk.CTkButton(pack,text='Encontrar cliente',command='')
find_cliente.grid(row=3,column=0, pady= (10,0),sticky = 'ew')

dados_cliente = ctk.CTkButton(pack,text='Alterar dados do cliente',command='')
dados_cliente.grid(row=4,column=0, pady= (10,0),sticky = 'ew')

novo_dado = ctk.CTkButton(pack,text='Novo tipo de dado',command='')
novo_dado.grid(row=5,column=0, pady= (10,0),sticky = 'ew')


add_filial = ctk.CTkButton(pack2,text='Adicionar Filial',command='')
add_filial.grid(row=1,column=0, pady= (10,0),sticky = 'ew')

del_filial = ctk.CTkButton(pack2,text='Remover Filial',command='')
del_filial.grid(row=2,column=0, pady= (10,0),sticky = 'ew')

rename_filial = ctk.CTkButton(pack2,text='Renomear Filial',command='')
rename_filial.grid(row=3,column=0, pady= (10,0),sticky = 'ew')


cad_produto = ctk.CTkButton(pack3,text='Cadastrar produto',command='')
cad_produto.grid(row=1,column=0, pady= (10,0),sticky = 'ew')

del_produto = ctk.CTkButton(pack3,text='Remover produto',command='')
del_produto.grid(row=2,column=0, pady= (10,0),sticky = 'ew')

edit_produto = ctk.CTkButton(pack3,text='Alterar quantidade do produto',command='')
edit_produto.grid(row=3,column=0, pady= (10,0),sticky = 'ew')

vs_dados = ctk.CTkButton(pack,text='Visualizar Dados',command='')

vs_dados_inv = ctk.CTkButton(pack,text='Visualizar Dados da Filial',command='')

app.mainloop()