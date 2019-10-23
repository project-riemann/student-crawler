import requests
import random
from database.insert import insert_jovem, insert_carteira
from database.connection import connection
from database.create import create_db


def parse_item(response, item):
    return response.text.split(item)[1].split(
        "</strong>")[0].replace(" <strong>", "")


def remove_special(name):
    return name.replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U").replace("\n", "").replace("Ã", "A").replace("Â", "A").replace("Ê", "E").replace("Ç", "C").replace("Ô", "O").replace("Ì", "I")


lista = open("lista.txt", "r+")

dNascimento = ""
create_db(connection)

with open('lista.txt') as lista:
    for aluno in lista:
        dAluno = remove_special(aluno)

        data = {
            "dAluno": dAluno,
            "dNascimento": dNascimento,
            "pes": "1"
        }

        response = requests.post(
            "http://pe.carteirafacil.com.br/2015/aluno/solicita.php",
            data=data
        )
        try:
            pai = parse_item(response, "Pai ou Representante:")
            mae = parse_item(response, "Mãe:")
            data = parse_item(response, "Data Nasc:")[:10]
            instituicao = response.text.split("Aluno:")[0].split(
                "</h3>")[0].split("<h3>")[1].split("- ")[1]
            email = response.text.split("Repetir E-mail:")[1].split(
                "/>")[0].split("value=")[1].replace("\"", "")
            fake_cpf = random.randint(11111111111, 99999999999)

            insert_jovem(connection, fake_cpf, dAluno, data)
            insert_carteira(connection, fake_cpf, mae, pai, instituicao, email)
            print('Done', dAluno)
        except:
            print("User not found", dAluno)
