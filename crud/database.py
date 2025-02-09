import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error


load_dotenv()

password = os.getenv('password')

def connect():
    try: 
        conn = psycopg2.connect(
            user="postgres",
            password= password,
            port= "5432",
            database= "gestaoTorneios")
        
        print("Conexão sucedida ao postgres")

        return conn
    
    except Error as e:
        print(f"Erro ao conectar no banco de dados {e}")

def end_connection(conn):
    if conn:
        conn.close()
    print("Conexão encerrada com o banco de dados")