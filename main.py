import requests
import xmltodict
import pandas as pd
from sqlalchemy import create_engine


### mysql 연결
MYSQL_HOSTNAME = '192.168.115.200:3306'  # 내 mysql ip
MYSQL_USER = 'lcm'  # 내가 생성한 user
MYSQL_PASSWORD = 'qwer1234'
MYSQL_DATABASE = 'lcm_db'  # 내가 생성한 db
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string) #내 db에 정보를 넘겨줌

url = "http://openapi.seoul.go.kr:8088/4b4878424b646c6331394362647463/xml/TbCorona19CountStatusJCG/1/5/" #xml -> json
rows=['JONGNOADD', 'JUNGGUADD', 'YONGSANADD', 'GWANGJINADD', 'DDMADD', 'JUNGNANGADD', 'SEONGBUKADD', 'GANGBUKADD', 'DOBONGADD', 'NOWONADD','EPADD','SDMADD','MAPOADD','YANGCHEONADD','GANGSEOADD','GUROADD','GEUMCHEONADD','YDPADD','DONGJAKADD','GWANAKADD','SEOCHOADD','GANGNAMADD','SONGPAADD','GANGDONGADD', 'ETCADD']
columns = ['JONGNO', 'JUNGGU', 'YONGSAN', 'GWANGJIN', 'DDM', 'JUNGNANG', 'SEONGBUK', 'GANGBUK', 'DOBONG', 'NOWON','EP','SDM','MAPO','YANGCHEON','GANGSEO','GURO','GEUMCHEON','YDP','DONGJAK','GWANAK','SEOCHO','GANGNAM','SONGPA','GANGDONG', 'ETC']

req = requests.get(url).content
xmlObject = xmltodict.parse(req)
dict_data = xmlObject['TbCorona19CountStatusJCG']['row']
df_conf = pd.DataFrame(dict_data)
df_conf = pd.melt(df_conf,
                  id_vars=['JCG_DT'],
                  value_vars=rows,
                  value_name='con',
                  ignore_index=False)

df_conf_1 = df_conf.astype(
    {'JCG_DT': 'datetime64', "con": "int"})
df_conf_1.to_sql(name='test16', con=db, if_exists = 'replace', index= False)
db.execute('ALTER TABLE test16 ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')

print(df_conf_1)




