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
        print("Insertion inepe done", cpf, NU_INSCRICAO, NU_ANO)
    except Exception as e:
        print("error trying to insert", cpf, NU_INSCRICAO, NU_ANO)
        print(e)

def insert_enem(connection, cpf, NU_INSCRICAO, NU_ANO, TP_SEXO, NACIONALIDADE, TP_ESCOLA, TP_ESTADO_CIVIL, renda_mensal, pessoas_na_casa, residencia_tipo, numero_tvs, numero_computadores, numero_automoveis, numero_geladeira, numero_telefone_fixo, numero_acesso_internet, numero_tv_assinatura, numero_aspirador_po, numero_empregados, numero_banheiros, ja_exerceu_ativ_remunerada):
    cursor = connection.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO Enem
            (cpf, NU_INSCRICAO, NU_ANO, TP_SEXO, NACIONALIDADE, TP_ESCOLA, TP_ESTADO_CIVIL, renda_mensal, pessoas_na_casa, residencia_tipo, numero_tvs, numero_computadores, numero_automoveis, numero_geladeira, numero_telefone_fixo, numero_acesso_internet, numero_tv_assinatura, numero_aspirador_po, numero_empregados, numero_banheiros, ja_exerceu_ativ_remunerada)
            VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");
            '''.format(cpf, NU_INSCRICAO, NU_ANO, TP_SEXO, NACIONALIDADE, TP_ESCOLA, TP_ESTADO_CIVIL, renda_mensal, pessoas_na_casa, residencia_tipo, numero_tvs, numero_computadores, numero_automoveis, numero_geladeira, numero_telefone_fixo, numero_acesso_internet, numero_tv_assinatura, numero_aspirador_po, numero_empregados, numero_banheiros, ja_exerceu_ativ_remunerada)
        )
        connection.commit()
        print("Insertion enem done", cpf, NU_INSCRICAO, NU_ANO, TP_SEXO, NACIONALIDADE, TP_ESCOLA, TP_ESTADO_CIVIL, renda_mensal, pessoas_na_casa, residencia_tipo, numero_tvs, numero_computadores, numero_automoveis, numero_geladeira, numero_telefone_fixo, numero_acesso_internet, numero_tv_assinatura, numero_aspirador_po, numero_empregados, numero_banheiros, ja_exerceu_ativ_remunerada)
    except Exception as e:
        print("error trying to insert", cpf, NU_INSCRICAO, NU_ANO, TP_SEXO, NACIONALIDADE, TP_ESCOLA, TP_ESTADO_CIVIL, renda_mensal, pessoas_na_casa, residencia_tipo, numero_tvs, numero_computadores, numero_automoveis, numero_geladeira, numero_telefone_fixo, numero_acesso_internet, numero_tv_assinatura, numero_aspirador_po, numero_empregados, numero_banheiros, ja_exerceu_ativ_remunerada)
        print(e)
