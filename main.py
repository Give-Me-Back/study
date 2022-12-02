import urllib.request
import json
import pandas as pd
from sqlalchemy import create_engine
from pandas import DataFrame
import datetime
import pymysql
from pandas.io.json import json_normalize

def data_insert():
    ### mysql 연결
    MYSQL_HOSTNAME = '192.168.115.200:3306'  # 내 mysql ip
    MYSQL_USER = 'lcm'  # 내가 생성한 user
    MYSQL_PASSWORD = 'qwer1234'
    MYSQL_DATABASE = 'lcm_db'  # 내가 생성한 db
    connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
    db = create_engine(connection_string) #내 db에 정보를 넘겨줌
    test.to_sql(name='test', con=db, index=False) #내 db에 정보 insert

url = "http://openapi.seoul.go.kr:8088/4b4878424b646c6331394362647463/json/TbCorona19CountStatusJCG/1/5/" #xml -> json
rows=['JONGNOADD', 'JUNGGUADD', 'YONGSANADD', 'GWANGJINADD', 'DDMADD', 'JUNGNANGADD', 'SEONGBUKADD', 'GANGBUKADD', 'DOBONGADD', 'NOWONADD','EPADD','SDMADD','MAPOADD','YANGCHEONADD','GANGSEOADD','GUROADD','GEUMCHEONADD','YDPADD','DONGJAKADD','GWANAKADD','SEOCHOADD','GANGNAMADD','SONGPAADD','GANGDONGADD', 'ETCADD']
columns = ['JONGNO', 'JUNGGU', 'YONGSAN', 'GWANGJIN', 'DDM', 'JUNGNANG', 'SEONGBUK', 'GANGBUK', 'DOBONG', 'NOWON','EP','SDM','MAPO','YANGCHEON','GANGSEO','GURO','GEUMCHEON','YDP','DONGJAK','GWANAK','SEOCHO','GANGNAM','SONGPA','GANGDONG', 'ETC']

response = urllib.request.urlopen(url)
json_str = response.read().decode("UTF-8")
json_object = json.loads(json_str)
df = pd.json_normalize(json_object['TbCorona19CountStatusJCG']['row'])
#json_str string 타입, json_object dict 타입.

df_change = df.T
test = df_change.loc[rows]
test2 = df_change.loc[columns]

#df_test = {'city':columns, 'virus':} #test[0]는 도시 : 확진자수로 묶여있다.
#df_final = DataFrame(df_test)
print(df_change.columns)
#print(df)
#data_insert()

for i in df.columns:
    test_columns = list(df.columns)
    #데이터 프레임에서 칼럼명을 뽑아서 저장.





