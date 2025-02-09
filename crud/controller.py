from database import connect, end_connection
from datetime import datetime, date

connection = connect()
cursor = connection.cursor()

# CREATE
"""
Insere novos registros na tabela especificada.
:param table: O nome da tabela onde os dados serão inseridos.
:param columns: Uma lista com os nomes das colunas onde os valores serão inseridos.
:param values: Uma lista de tuplas com os valores correspondentes às colunas.
"""
def insert(table, columns, values):
    placeholders = ', '.join(['%s'] * len(columns))
    columns_str = ', '.join(columns)
    cmd_insert = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
    cursor.executemany(cmd_insert, values)
    connection.commit()
    print(f"Dados inseridos com sucesso na tabela {table}")

# READ
"""
Recupera todos os registros de uma tabela e colunas especificadas.
:param table: O nome da tabela a ser consultada.
:param columns: Uma lista com os nomes das colunas a serem recuperadas.
:param join_clause: Uma lista de tuplas onde a tupla é (tabela, associacao, associacao)
:param condition: Possui a condição para ser utilizado no WHERE
:param order_by: Lista de 2 posições, posição 1 = coluna, posição 2 = ASC ou DESC
:return: Uma lista de tuplas contendo os dados consultados.
"""
def get_all(table, columns, join_clause=None, condition=None, order_by=None):
    columns_str = ', '.join(columns)
    cmd_get = f"SELECT {columns_str} FROM {table}"

    if join_clause:
        for join_tuple in join_clause:
            cmd_get += f" JOIN {join_tuple[0]} ON {join_tuple[1]} = {join_tuple[2]}"

    if condition:
        cmd_get += f" WHERE {condition}"

    if order_by:
        cmd_get += f" ORDER BY {order_by[0]} {order_by[1]}"

    cursor.execute(cmd_get)
    results = cursor.fetchall()
    '''for row in results:
        print(row)'''
    return results

# UPDATE
"""
Atualiza registros na tabela especificada com base em condições fornecidas.
:param table: O nome tabela onde os dados serão atualizados.
:param update: Um dicionário contendo pares como coluna-valor para atualizar.
:param condition: Um dicionário contendo pares como coluna-valor para a cláusula WHERE.
"""
def update(table, update, condition):
    set_clause = ', '.join([f"{i} = %s" for i in update.keys()])
    where_clause = ' AND '.join([f"{i} = %s" for i in condition.keys()])
    cmd_update = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
    values = list(update.values()) + list(condition.values())
    cursor.execute(cmd_update, values)
    connection.commit()
    print(f"Dados atualizados na tabela {table}")

# DELETE
"""
Deleta registros da tabela soloicitada com base em condições fornecidas.
:param table: O nome da tabela de onde os registros serão deletados.
:param condition: Um dicionário contendo pares como coluna-valor para a cláusula WHERE.
"""
def delete(table, condition):
    where_clause = ' AND '.join([f"{i} = %s" for i in condition.keys()])
    cmd_delete = f"DELETE FROM {table} WHERE {where_clause}"
    values = list(condition.values())
    cursor.execute(cmd_delete, values)
    connection.commit()
    print(f"Dados deletados da tabela {table}")


regexData = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

def criar_partidas(cod_torneio):
    
    return

if __name__ == "__main__":
    # Teste de usos

    #insert("organizadores", ["codorganizador", "nome"], [(30, "Ferreora")])

    # Teste SELECT *
    #get_all("organizadores", ["*"], None, None, None)

    # Teste SELECT somente com condition
    #get_all("organizadores", ["codorganizador", "nome"], None, "codorganizador = 10", None)

    # Teste SELECT somente com ORDER BY
    #get_all("organizadores", ["codorganizador", "nome"], None, None, ["codorganizador", "DESC"])

    # Teste SELECT com WHERE e ORDER BY
    #get_all("organizadores", ["codorganizador", "nome"], None, "codorganizador > 5", ["codorganizador", "DESC"])

    # Teste SELECT com JOIN, where e order by
    '''
    get_all(
            "torneio", ["torneio.nome", "regiao.localizacao", "tier.nivel", "regiao.localizacao", "organizadores.nome"],
            [("tier", "tier.codtier", "torneio.codtorneio"),
                ("regiao", "regiao.codRegiao", "torneio.codRegiao"),
                ("torneio_organizadores", "torneio_organizadores.codtorneio", "torneio.codtorneio"),
                ("organizadores", "torneio_organizadores.codorganizadorr", "organizadores.codorganizador")
                ],
            "torneio.nome = 'Champions 2025'",
            ["organizadores.nome", "DESC"])
    '''

    #insert('torneio', ['codtorneio', 'nome', 'datainicial', 'datafinal', 'codregiao', 'codtier'], [("7", "Rio de Janeiro Qualifiers", "2025-01-01", "2025-02-02", "1", "1")])  
    #insert("organizadores", ["codorganizador", "nome"], "")

    #print(datetime.date(2023, 10, 1))