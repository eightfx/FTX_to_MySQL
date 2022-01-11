import os

import pymysql
from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

load_dotenv()
pymysql.install_as_MySQLdb()
# mysqlのDBの設定
DATABASE = '{}'.format(
    os.environ['DATABASE_URL'],
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=False# Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
