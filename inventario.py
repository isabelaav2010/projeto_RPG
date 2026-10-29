"""
inventario.py - Funções da tabela INVENTARIO.   (DESAFIO)

Colunas: id, personagem_id, item_id, quantidade

"""

def incluir(conn, personagem_id, item_id, quantidade):
    """Coloca um item no inventário de um personagem e devolve o id gerado."""
    cursor = conn.execute("INSERT INTO inventario (item_id, personagem_id, quantidade),  VALUES (?, ?, ?)",
     (item_id, personagem_id, quantidade,))
    conn.commit()                 # grava de verdade no arquivo
    return cursor.lastrowid

def buscar_por_id(conn, id):
    """Devolve UMA linha, ou None."""
    cursor = conn.execute("SELECT id, personagem_id, item_id, quantidade FROM inventario WHERE id = ?", (id,))
    return cursor.fetchone()

def buscar_por_nome(conn, nome_personagem):
    """Devolve uma LISTA com os itens dos personagens cujo nome contém o texto."""
    cursor = conn.execute(
    """
    SELECT itens.id, inventario.quantidade, personagens.id FROM inventario JOIN personagens ON inventario.personagem_id = personagens.id WHERE personagens.nome LIKE ?
    "ORDER BY personagens.nome
    """,
    ("%" + nome_personagem + "%",))
    return cursor.fetchall()

def listar(conn):
    """Devolve uma LISTA com todo o inventário."""
    cursor = conn.execute(
    """
    SELECT inventario.id, personagens.nome, itens.nome, itens.tipo, inventario.quantidade
    FROM inventario JOIN personagens ON inventario.personagem_id = personagens.id 
    JOIN itens ON inventario.item_id = itens.id 
    ORDER BY inventario.id
    """)
    return cursor.fetchall()
