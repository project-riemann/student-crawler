import requests


def parse_item(response, item):
    return response.text.split(item)[1].split(
        "</strong>")[0].replace(" <strong>", "")


dAluno = input("nome: ")
dNascimento = ""

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
    data = parse_item(response, "Data Nasc:")
    instituicao = response.text.split("Aluno:")[0].split(
        "</h3>")[0].split("<h3>")[1].split("- ")[1]
    email = response.text.split("Repetir E-mail:")[1].split(
        "/>")[0].split("value=")[1].replace("\"", "")

    print(data)
    print(pai)
    print(mae)
    print(instituicao)
    print(email)
except:
    print("User not found")
