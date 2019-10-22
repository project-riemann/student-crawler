def insert_jovem(connection, cpf, nome, data_nascimento):
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO Jovem
            (cpf, nome, data_nascimento)
            VALUES("{}", "{}", "{}");
            '''.format(cpf, nome, data_nascimento)
        )
        connection.commit()
        print("Insertion jovem done", cpf, nome, data_nascimento)
    except Exception as e:
        print("error trying to insert", cpf, nome, data_nascimento)
        print(e)

def insert_carteira(connection, cpf, nome_mae, nome_pai, instituicao, email):
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO Carteira_Estudante
            (cpf, nome_mae, nome_pai, instituicao, email)
            VALUES("{}", "{}", "{}", "{}", "{}");
            '''.format(cpf, nome_mae, nome_pai, instituicao, email)
        )
        connection.commit()
        print("Insertion carteira done", cpf, nome_mae, nome_pai, instituicao, email)
    except Exception as e:
        print("error trying to insert", cpf, nome_mae, nome_pai, instituicao, email)
        print(e)

def insert_inep(connection, cpf, NU_INSCRICAO, NU_ANO):
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO Inep
            (cpf, NU_INSCRICAO, NU_ANO)
            VALUES("{}", "{}", "{}");
            '''.format(cpf, NU_INSCRICAO, NU_ANO)
        )
        connection.commit()
        print("Insertion inpe done", cpf, NU_INSCRICAO, NU_ANO)
    except Exception as e:
        print("error trying to insert", cpf, NU_INSCRICAO, NU_ANO)
        print(e)


