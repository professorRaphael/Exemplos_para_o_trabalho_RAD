import sqlite3


def connect():
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS livro (id INTEGER PRIMARY KEY, titulo text, autor text, ano integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(titulo, autor, ano, isbn):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO livro VALUES (NULL,?,?,?,?)",
                (titulo, autor, ano, isbn))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM livro")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(titulo="", autor="", ano="", isbn=""):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM livro WHERE titulo=? OR autor=? OR ano=? OR isbn=?",
                (titulo, autor, ano, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM livro WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, titulo, autor, ano, isbn):
    conn = sqlite3.connect("livros.db")
    cur = conn.cursor()
    cur.execute("UPDATE livro SET titulo=?, autor=?, ano=?, isbn=? WHERE id=?",
                (titulo, autor, ano, isbn, id))
    conn.commit()
    conn.close()


connect()
