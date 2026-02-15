import sqlite3

# criar base de dados
connection = sqlite3.connect("minimercado.db")

# ligar base de de dados e criar tabela
cursor = connection.cursor()
cursor.execute("CREATE TABLE clientes (pnome TEXT, unome TEXT, contribuinte INTEGER)")

# introduzir registos na tabela
cursor.execute("INSERT INTO clientes VALUES ('Coco', 'Chanel', 571026119)")
cursor.execute("INSERT INTO clientes VALUES ('Pablo', 'Picasso', 628169274)")
cursor.execute("INSERT INTO clientes VALUES ('Greta', 'Thunberg', 105103539)")
cursor.execute("INSERT INTO clientes VALUES ('Roger', 'Federer', 372219876)")

print(connection.total_changes)

rows = cursor.execute("SELECT pnome, unome, contribuinte FROM clientes").fetchall()
print(rows)


#%% selecionar registo
target_clientes_pnome = "Pablo"
rows = cursor.execute(
    "SELECT pnome, unome, contribuinte FROM clientes WHERE pnome = ?",
    (target_clientes_pnome,),
).fetchall()
print(rows)


#%% atualizar registo
novo_contribuinte = 236827190
pnome_update = "Coco"
cursor.execute(
    "UPDATE clientes SET contribuinte = ? WHERE pnome = ?",
    (novo_contribuinte, pnome_update)
)

rows = cursor.execute("SELECT pnome, unome, contribuinte FROM clientes").fetchall()
print(rows)


#%% remover registo
pnome_remove = "Roger"
cursor.execute(
    "DELETE FROM clientes WHERE pnome = ?",
    (pnome_remove,)
)

rows = cursor.execute("SELECT pnome, unome, contribuinte FROM clientes").fetchall()
print(rows)


#%% converter tabela para ficheiro texto
import pandas as pd

dbdf = pd.read_sql("SELECT * FROM clientes", connection)

dbdf.to_csv('clientes.csv', index=False)


#%% fechar ligacao e base de dados
connection.commit()
cursor.close
connection.close()
