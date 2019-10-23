# install with python3 -m pip install PyMySQL
from connection import connection
from create import create_db
from insert import insert_jovem, insert_carteira, insert_inep, insert_enem

create_db(connection)
insert_jovem(connection, "10097142441",
             "Otacilio Saraiva Maia Neto", "14/12/1996")
insert_carteira(connection, "10097142441", "Dona Faker",
                "Seu Sumido", "Cesinha School", "osmn@cesar.school")
insert_inep(connection, "10097142441", "1218721872128", "2017")
#                      CPF  MASCULINO  Br Pub Single Rico 20 urbana 1tv 3pcs no_car 1   2  net   tv  po emprega banh trablh
insert_enem(connection, "10097142441", "1218721872128", "2017", "M", 1, 1,
            0, "Q", 20, "B", "A", "C", "D", "A", "B", "A", "A", "D", "C", "B", "A")
# Guardar dados em memoria pra inserir de vez

connection.close()
