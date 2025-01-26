from database import connect, end_connection


def main():
    connection = connect()
    cursor = connection.cursor()

    # CREATE
    """
    Insere um novo registro na tabela especificada.
    :param table: O nome da tabela onde os dados serão inseridos.
    :param columns: Uma lista com os nomes das colunas onde os valores serão inseridos.
    :param values: Uma lista com os valores correspondentes às colunas.
    """
    def insert(table, columns, values):
        placeholders = ', '.join(['%s'] * len(values))
        columns_str = ', '.join(columns)
        cmd_insert = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        cursor.execute(cmd_insert, values)
        connection.commit()
        print(f"Dados inseridos com sucesso na tabela {table}")

    # READ
    """
    Recupera todos os registros de uma tabela e colunas especificadas.
    :param table: O nome da tabela a ser consultada.
    :param columns: Uma lista com os nomes das colunas a serem recuperadas.
    :return: Uma lista de tuplas contendo os dados consultados.
    """
    def get_all(table, columns):
        columns_str = ', '.join(columns)
        cmd_get = f"SELECT {columns_str} FROM {table}"
        cursor.execute(cmd_get)
        results = cursor.fetchall()
        for row in results:
            print(row)
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

    # Teste de usos
    #insert("jogadores", ["bid", "nome", "time", "posicao", "data_nascimento"], ["EFGH", "Carlos Silva", "Flamengo", "Zagueiro", "15/09/1998"])
    insert("patrocinadores", ["identificador", "nome"], [20, "Guaravita"])
    #get_all("patrocinadores", ["nome"])
    #get_all("jogadores", ["time", "posicao", "nome"])
    #update("jogadores", {"time": "São Paulo", "posicao": "Zagueiro"}, {"bid" : "EFGH"})
    #delete("jogadores", {"bid": "EFGH"})


if __name__ == "__main__":
    main()