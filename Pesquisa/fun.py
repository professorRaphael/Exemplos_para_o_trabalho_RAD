#=====================================BIBLIOTECAS==============================================
from tkinter import Tk, Frame, TOP, StringVar, SOLID, LEFT, RIGHT, X, Y, Label, Entry, Button, Scrollbar, HORIZONTAL, VERTICAL, BOTTOM, NO, W
import sqlite3
import tkinter.ttk as ttk

#=====================================TELA==============================================
root = Tk()
root.title("Exemplo de pesquisa")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

#=====================================METODOS==============================================
def base_de_dados():
    conn = sqlite3.connect("./python.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `membros` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, nome TEXT, email TEXT, endereco TEXT, idade TEXT)")
    cursor.execute("SELECT * FROM `membros`")
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Raphael', 'raphael.jesus@email.com', 'Rio de Janeiro', '36')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Carol', 'Carol@email', 'Rio de Janeiro', '27')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Ikit', 'Ikit@Claw', 'Skavenblight', '180')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Thorgrim', 'Thorgrim@Grudgebearer', 'Karaz-a-Karak', '355')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Tyrion', 'Tyrion@PhoenixKing', 'Lothern', '222')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Karl', 'Karl@Franz', 'Altdorf', '30')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Gelt', 'Balthasar@Gelt', 'Altdorf', '30')")
        cursor.execute(
            "INSERT INTO `membros` (nome, email, endereco, idade) VALUES('Grimgor', 'Grimgor@Ironhide', 'Blasted Wastes', '300')")
        conn.commit()

    cursor.execute("SELECT * FROM `membros` ORDER BY `email` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def pesquisar():
    if procura.get() != "":
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("./python.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `membros` WHERE `nome` LIKE ? OR `email` LIKE ?",
                       ('%'+str(procura.get())+'%', '%'+str(procura.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()


def limpa():
    conn = sqlite3.connect("./python.db")
    cursor = conn.cursor()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `membros` ORDER BY `email` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


#=====================================VARIAVEIS============================================
procura = StringVar()

#=====================================FRAME================================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
TopFrame = Frame(root, width=500)
TopFrame.pack(side=TOP)
TopForm = Frame(TopFrame, width=300)
TopForm.pack(side=LEFT, pady=10)
TopMargin = Frame(TopFrame, width=260)
TopMargin.pack(side=LEFT)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)

#=====================================LABEL =========================================
lbl_title = Label(Top, width=500, font=('arial', 18),
                  text="Exemplo de filtro")
lbl_title.pack(side=TOP, fill=X)

#=====================================ENTRY =========================================
procura = Entry(TopForm, textvariable=procura)
procura.pack(side=LEFT)

#=====================================BUTTON ========================================
btn_procura = Button(TopForm, text="Pesquisar", bg="#006dcc", command=pesquisar)
btn_procura.pack(side=LEFT)
btn_limpar = Button(TopForm, text="Limpar", command=limpa)
btn_limpar.pack(side=LEFT)
#=====================================TABELA =========================================
scrollbarx = Scrollbar(MidFrame, orient=HORIZONTAL)
scrollbary = Scrollbar(MidFrame, orient=VERTICAL)
tree = ttk.Treeview(MidFrame, columns=("membrosID", "nome", "email", "endereco", "idade"),
                    selectmode="extended", height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('membrosID', text="membrosID", anchor=W)
tree.heading('nome', text="nome", anchor=W)
tree.heading('email', text="email", anchor=W)
tree.heading('endereco', text="endereco", anchor=W)
tree.heading('idade', text="idade", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=170)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.pack()

#=====================================INICIA=======================================
if __name__ == '__main__':
    base_de_dados()
    root.mainloop()
