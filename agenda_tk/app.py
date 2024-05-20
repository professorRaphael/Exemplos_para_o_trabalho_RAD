import tkinter.ttk as ttk
import tkinter.messagebox as msb
from tkinter import Tk, Label, StringVar, Entry, Scrollbar, Button, Toplevel, Frame, TOP, LEFT, RIGHT, X, W, Y, BOTTOM, SOLID, HORIZONTAL, VERTICAL, NO, Menu
import sqlite3
import os

# --------- FRAMES - PRINCIPAL -------------
root = Tk()
root.title("**** LISTA DE CONTATOS *****")
width = 700
height = 400
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
# root.geometry(f'{width}x{height}+{x}+{y}')
root.resizable(0,0)
# Obtém o diretório atual do script
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# Define o nome do arquivo .ico
icone_filename = "icons8_user.ico"
# Combina o diretório atual com o nome do arquivo .ico
caminho_icone = os.path.join(diretorio_atual, icone_filename)
root.iconbitmap(caminho_icone)
root.config(bg='#6666ff')

# --------- VARIAVEIS -------------

'''
x = StringVar() # armazena uma string; valor padrâo ""
x = IntVar() # armazena um integer; valor padrâo 0
x = DoubleVar() # armazena um float; valor padrão 0.0
x = BooleanVar() # armazena um boolean, retorna 0 se for False e 1 se for True
'''
nome = StringVar()
telefone = StringVar()
idade = StringVar()
email = StringVar()
endereco = StringVar()

'''
As duas grandes vantagens que essas variáveis têm são: 
Você pode associar uma variável a mais de um widget, 
para que dois ou mais widgets exibam exatamente as mesmas informações o tempo todo. 
Você pode vincular funções a serem chamadas quando os valores mudarem.
'''

id = None
janela_alterar = None
janela_incluir = None
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
banco_filename = "contatos.sqlite"
caminho_db = os.path.join(diretorio_atual, banco_filename)

# --------- METODOS -------------

def database():
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'humanos' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT, telefone TEXT, idade TEXT, email TEXT, endereco TEXT) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
    buscar = cursor.fetchall()
    for data in buscar:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def enviar_dados():
    if nome.get() == "" or telefone.get() == "" or idade.get() == "" or email.get() == "" or endereco.get() == "":
        msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect(caminho_db)
        cursor = conn.cursor()
        query = """ INSERT INTO 'humanos' (nome, telefone, idade, email, endereco) VALUES(?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        telefone.set("")
        idade.set("")
        email.set("")
        endereco.set("")


def alterar_dados():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect(caminho_db)
    cursor = conn.cursor()
    cursor.execute(""" UPDATE 'humanos' SET nome = ?, telefone = ?, idade = ?, email = ?, endereco = ? WHERE id = ?""",
                   (str(nome.get()), str(telefone.get()), str(idade.get()), str(email.get()), str(endereco.get()), int(id)))
    conn.commit()
    cursor.execute("SELECT * FROM 'humanos' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    janela_alterar.destroy()


def selecionar_dado(event):
    global id, janela_alterar
    item = tree.focus()
    conteudo = (tree.item(item))
    item_selecionado = conteudo['values']
    id = item_selecionado[0]
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    nome.set(item_selecionado[1])
    telefone.set(item_selecionado[2])
    idade.set(item_selecionado[3])
    email.set(item_selecionado[4])
    endereco.set(item_selecionado[5])
    # --------- FRAMES - ATUALIZAR -------------
    janela_alterar = Toplevel()
    janela_alterar.title("**** ATUALIZANDO CONTATO *****")
    form_titulo = Frame(janela_alterar)
    form_titulo.pack(side=TOP)
    form_contato = Frame(janela_alterar)
    form_contato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = janela_alterar.winfo_screenwidth()
    sc_height = janela_alterar.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    janela_alterar.geometry("%dx%d+%d+%d" % (width, height, x, y))
    janela_alterar.resizable(0, 0)

    # --------- LABELS - ATUALIZAR -------------
    lbl_title = Label(form_titulo, text="Atualizando contatos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(form_contato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(form_contato, text='Telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(form_contato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(form_contato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(form_contato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    # --------- ENTRY - ATUALIZAR -------------

    nome_entry = Entry(form_contato, textvariable=nome, font=('arial', 12))
    nome_entry.grid(row=0, column=1)
    telefone_entry = Entry(form_contato, textvariable=telefone, font=('arial', 12))
    telefone_entry.grid(row=1, column=1)
    idade_entry = Entry(form_contato, textvariable=idade, font=('arial', 12))
    idade_entry.grid(row=2, column=1)
    email_entry = Entry(form_contato, textvariable=email, font=('arial', 12))
    email_entry.grid(row=3, column=1)
    endereco_entry = Entry(form_contato, textvariable=endereco, font=('arial', 12))
    endereco_entry.grid(row=4, column=1)
    # --------- BOTÃO - ATUALIZAR -------------
    bttn_atualizando = Button(form_contato, text="Atualizar",
                            width=50, command=alterar_dados)
    bttn_atualizando.grid(row=6, columnspan=2, pady=10)


# --------- METODO - DELETAR -------------
def apagar_dado():
    if not tree.selection():
        msb.showwarning('ALERTA DE ERRO', 'Por favor, selecione o item na lista.', icon='warning')
    else:
        resultado = msb.askquestion('', 'Tem certeza que deseja deletar o contato?')
        if resultado == 'yes':
            item = tree.focus()
            conteudo = (tree.item(item))
            item_selecionado = conteudo['values']
            tree.delete(item)
            conn = sqlite3.connect(caminho_db)
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM 'humanos' WHERE id = {item_selecionado[0]}")
            conn.commit()
            cursor.close()
            conn.close()


def inserir_dados():
    global janela_incluir
    nome.set("")
    telefone.set("")
    idade.set("")
    email.set("")
    endereco.set("")
    # --------- FRAMES - CADASTRAR -------------
    janela_incluir = Toplevel()
    janela_incluir.title("**** INSERINDO CONTATO *****")
    form_titulo = Frame(janela_incluir)
    form_titulo.pack(side=TOP)
    form_contato = Frame(janela_incluir)
    form_contato.pack(side=TOP, pady=10)
    width = 400
    height = 300
    sc_width = janela_incluir.winfo_screenwidth()
    sc_height = janela_incluir.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    janela_incluir.geometry("%dx%d+%d+%d" % (width, height, x, y))
    janela_incluir.resizable(0, 0)

    # --------- LABELS - CADASTRAR -------------
    lbl_title = Label(form_titulo, text="Inserindo contatos",
                      font=('arial', 18), bg='blue', width=280)
    lbl_title.pack(fill=X)
    lbl_nome = Label(form_contato, text='Nome', font=('arial', 12))
    lbl_nome.grid(row=0, sticky=W)
    lbl_telefone = Label(form_contato, text='Telefone', font=('arial', 12))
    lbl_telefone.grid(row=1, sticky=W)
    lbl_idade = Label(form_contato, text='Idade', font=('arial', 12))
    lbl_idade.grid(row=2, sticky=W)
    lbl_email = Label(form_contato, text='Email', font=('arial', 12))
    lbl_email.grid(row=3, sticky=W)
    lbl_endereco = Label(form_contato, text='Endereco', font=('arial', 12))
    lbl_endereco.grid(row=4, sticky=W)

    # --------- ENTRY - CADASTRAR -------------
    nome_entry = Entry(form_contato, textvariable=nome, font=('arial', 12))
    nome_entry.grid(row=0, column=1)
    nome_entry.focus()
    telefone_entry = Entry(form_contato, textvariable=telefone, font=('arial', 12))
    telefone_entry.grid(row=1, column=1)
    idade_entry = Entry(form_contato, textvariable=idade, font=('arial', 12))
    idade_entry.grid(row=2, column=1)
    email_entry = Entry(form_contato, textvariable=email, font=('arial', 12))
    email_entry.grid(row=3, column=1)
    endereco_entry = Entry(form_contato, textvariable=endereco, font=('arial', 12))
    endereco_entry.grid(row=4, column=1)
    # --------- BOTÃO - CADASTRAR -------------
    bttn_enviardados = Button(form_contato, text="Cadastrar",
                            width=50, command=enviar_dados)
    bttn_enviardados.grid(row=6, columnspan=2, pady=10)


# ---------------- FRAME PRINCIPAL -------------
topo = Frame(root, width=500, bd=1, relief=SOLID)
topo.pack(side=TOP)
mid = Frame(root, width=500, bg='#6666ff')
mid.pack(side=TOP)
meia_esquerda = Frame(mid, width=100)
meia_esquerda.pack(side=LEFT, pady=10)
meia_esquerdaPadding = Frame(mid, width=350, bg="#6666ff")
meia_esquerdaPadding.pack(side=LEFT)
meia_direita = Frame(mid, width=100)
meia_direita.pack(side=RIGHT, pady=10)
bottom = Frame(root, width=500)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# --------------- LABELS PRINCIPAL --------------
lbl_title = Label(topo, text="SISTEMA DE GERENCIAMENTO DE CONTATOS", font=('arial', 18), width=500)
lbl_title.pack(fill=X)

lbl_alterar = Label(bottom, text="Para alterar clique duas vezes no contato desejado.", font=('arial', 12), width=200)
lbl_alterar.pack(fill=X)

# --------------- BUTTONS PRINCIPAL --------------
bttn_add = Button(meia_esquerda, text="INSERIR", bg="royal blue", command=inserir_dados)
bttn_add.pack()
bttn_apagar = Button(meia_direita, text="APAGAR",
                     bg="OrangeRed2", command=apagar_dado)
bttn_apagar.pack(side=RIGHT)

# --------------- TREEVIEW PRINCIPAL --------------

ScrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
ScrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Nome", "Telefone", "Idade", "Email", "Endereço"),
                    height=400, selectmode="extended", yscrollcommand=ScrollbarY.set, xscrollcommand = ScrollbarX.set)
ScrollbarY.config(command=tree.yview)
ScrollbarY.pack(side=RIGHT, fill=Y)
ScrollbarX.config(command=tree.xview)
ScrollbarX.pack(side=BOTTOM, fill=X)
tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Telefone", text="Telefone", anchor=W)
tree.heading("Idade", text="Idade", anchor=W)
tree.heading("Email", text="Email", anchor=W)
tree.heading("Endereço", text="Endereço", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()
tree.bind('<Double-Button-1>', selecionar_dado)

# --------- MENU - PRINCIPAL ---------------
menu_bar = Menu(root)
root.config(menu=menu_bar)

# adicionar itens
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Criar novo", command=inserir_dados)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.destroy)

menuSobre = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Sobre", menu=menuSobre)
menuSobre.add_command(label="Info")


if __name__ == '__main__':
    database()
    root.mainloop()
