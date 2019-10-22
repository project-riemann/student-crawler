def create_db(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT cpf, nome, data_nascimento FROM students.Jovem;")
        print("DB Already exists")
    except:
        try:
            print("DB Not Exists, initializing...")
            cursor.execute(
                '''
    
                CREATE TABLE Jovem
                (
                    cpf VARCHAR(11) NOT NULL,
                    nome VARCHAR(90) NULL,
                    data_nascimento VARCHAR(10) NULL,
                    PRIMARY KEY (cpf)
                );
                '''
            )
            cursor.execute(
                '''
                CREATE TABLE Carteira_Estudante
                (
                    cpf VARCHAR(11) NOT NULL,
                    CONSTRAINT fk_carteira_estudante_cpf FOREIGN KEY(cpf) REFERENCES Jovem(cpf),
                    nome_mae VARCHAR(90) NULL,
                    nome_pai VARCHAR(90) NULL,
                    instituicao VARCHAR(90) NULL,
                    email VARCHAR(60) NULL,
                    PRIMARY KEY(cpf)
                );
                '''
            )
            cursor.execute(
                '''
                CREATE TABLE Inep
                (
                    cpf VARCHAR(11) NOT NULL,
                    CONSTRAINT fk_inep_cpf FOREIGN KEY(cpf) REFERENCES Jovem(cpf),
                    NU_INSCRICAO VARCHAR(13) NOT NULL,
                    NU_ANO VARCHAR(5) NOT NULL,
                    PRIMARY KEY(cpf, NU_INSCRICAO, NU_ANO)
                );
                '''
            )
            cursor.execute(
                '''
                CREATE TABLE Enem
                (
                    cpf VARCHAR(11) NOT NULL,
                    NU_INSCRICAO VARCHAR(13) NOT NULL,
                    NU_ANO VARCHAR(5) NOT NULL,
                    CONSTRAINT fk_enem_nu FOREIGN KEY(cpf, NU_INSCRICAO, NU_ANO) REFERENCES Inep(cpf, NU_INSCRICAO, NU_ANO),
                    TP_SEXO VARCHAR(1) NULL,
                    NACIONALIDADE INT(4) NOT NULL,
                    TP_ESCOLA INT(2) NOT NULL,
                    TP_ESTADO_CIVIL INT(4) NOT NULL,
                    renda_mensal VARCHAR(1) NOT NULL,
                    pessoas_na_casa INT(6) NOT NULL,
                    residencia_tipo VARCHAR(1) NOT NULL,
                    numero_tvs VARCHAR(1) NOT NULL,
                    numero_computadores VARCHAR(1) NOT NULL,
                    numero_automoveis VARCHAR(1) NOT NULL,
                    numero_geladeira VARCHAR(1) NOT NULL,
                    numero_telefone_fixo VARCHAR(1) NOT NULL,
                    numero_acesso_internet VARCHAR(1) NOT NULL,
                    numero_tv_assinatura VARCHAR(1) NOT NULL,
                    numero_aspirador_po VARCHAR(1) NOT NULL,
                    numero_empregados VARCHAR(1) NOT NULL,
                    numero_banheiros VARCHAR(1) NOT NULL,
                    ja_exerceu_ativ_remunerada VARCHAR(1) NOT NULL,
                    PRIMARY KEY(NU_INSCRICAO, NU_ANO)
                );
                '''
            )
            connection.commit()
            print("initialization done")
        except Exception as e:
            print("error trying to create database")
            print(e)