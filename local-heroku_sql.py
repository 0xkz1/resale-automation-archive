import pandas as pd
import psycopg2
from sqlalchemy import create_engine


# Heroku Postgresのコンフィグ
connection_config = {
    'host': '[DB_HOST_MASKED]',
    'database': '[DB_NAME_MASKED]',
    'user': '[DB_USER_MASKED]',
    'port': '5432',
    'password': '[DB_PASSWORD_MASKED]'
}
global engine
engine = create_engine(
    'postgres://[DB_USER_MASKED]:[DB_PASSWORD_MASKED]@[DB_HOST_MASKED]:5432/[DB_NAME_MASKED]'.
        format(**connection_config))
#sr = pd.Series('category':[[2],[3],[4]])

# PostgreSQLに接続する
con = psycopg2.connect(**connection_config)


# 事前にローカルSQLからCSV出力後、Heroku Postgresに読み込ませる
df = pd.read_csv('market.csv')
df.to_sql('market', con=engine, if_exists='append',# or replace
          index=False)

df = pd.read_csv('atklist4.csv')
df.to_sql('atklist4',con=engine, if_exists='append',# or replace
          index=False)


