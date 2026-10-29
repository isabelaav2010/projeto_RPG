"""
personagens.py - Funções da tabela PERSONAGENS.

Colunas: id, nome, nivel, jogador_id, classe_id

"""

def incluir(conn, nome, nivel, jogador_id, classe_id):
    """Insere um personagem e devolve o id gerado."""
    cursor = conn.execute("INSERT INTO personagens (nome, nivel, jogador_id, classe_id) VALUES (?, ?, ?, ?)", 
    (nome, nivel, jogador_id, classe_id))
    conn.commit()                 # grava de verdade no arquivo
    return cursor.lastrowid


def buscar_por_id(conn, id):
    """Devolve UMA linha, ou None."""
    cursor = conn.execute(
    """
    SELECT personagens.id, personagens.nome, personagens.nivel, jogadores.apelido, classes.nome
    FROM personagens JOIN jogadores ON jogadores.id = personagens.jogador_id 
    JOIN classes ON classes.id = personagens.classe_id WHERE personagens.id = ?
    """, (id,))
    return cursor.fetchone()


def buscar_por_nome(conn, nome):
    """Devolve uma LISTA com os personagens cujo nome contém o texto."""
    cursor = conn.execute(
    """
    SELECT personagens.id, personagens.nome, personagens.nivel, jogadores.apelido, classes.nome 
    FROM personagens JOIN jogadores ON jogadores.id = personagens.jogador_id 
    JOIN classes ON classes.id = personagens.classe_id WHERE personagens.nome LIKE ?
    """, ("%" + nome + "%",))
    return cursor.fetchall()


def listar(conn):
    """Devolve uma LISTA com todos os personagens."""
    cursor = conn.execute(
    """
    SELECT personagens.id, personagens.nome, personagens.nivel, jogadores.apelido, classes.nome
    FROM personagens JOIN jogadores ON personagens.jogador_id = jogadores.id 
    JOIN classes ON personagens.classe_id = classes.id 
    ORDER BY personagens.id
    """)
    return cursor.fetchall()
