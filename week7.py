import pymysql
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:feng20000310@127.0.0.1:3306/testdb?charset=utf8')
print(engine)

formlist = pd.read_sql_query('show tables', con = engine)
print('testdb:','\n',formlist)

detail1 = pd.read_sql_table('meal_order_detail1',con = engine)
print('read_sql_table:',len(detail1))