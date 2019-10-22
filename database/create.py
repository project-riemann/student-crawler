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
            connection.commit()
            print("initialization done")
        except Exception as e:
            print("error trying to create database")
            print(e)