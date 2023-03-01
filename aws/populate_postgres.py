import os
import psycopg2

# Configurações de conexão
db_host = os.environ['postgres-database-1.cluster-co7dfuudlpna.us-east-1.rds.amazonaws.com']
db_port = os.environ['5432']
db_name = os.environ['template1']
db_user = os.environ['postgres']
db_pass = os.environ['database_1']

# Tenta se conectar ao banco de dados e executar uma consulta simples
try:
    conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_pass)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM information_schema.tables;")
    print(cur.fetchone()[0])
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if conn is not None:
        conn.close()
