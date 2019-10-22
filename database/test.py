# install with python3 -m pip install PyMySQL
from connection import connection
from create import create_db
from insert import insert_jovem, insert_carteira, insert_inep

create_db(connection)
insert_jovem(connection, "10097142441", "Otacilio Saraiva Maia Neto", "14/12/1996")
insert_carteira(connection, "10097142441", "Dona Faker", "Seu Sumido", "Cesinha School", "osmn@cesar.school")
insert_inep(connection, "10097142441", "1218721872128", "2017")

## Guardar dados em memoria pra inserir de vez

connection.close()
