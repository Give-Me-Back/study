### DB 유저 생성

```
CREATE DATABASE lcm_db;				
CREATE USER 'lcm'@'%' IDENTIFIED BY 'qwer1234';	
GRANT ALL PRIVILEGES ON lcm_db.* TO 'lcm'@'%';
FLUSH PRIVILEGES;
EXIT;
```

### mysql 연결

```
MYSQL_HOSTNAME = '192.168.115.200:3306'  # 내 mysql ip
MYSQL_USER = 'lcm'  # 내가 생성한 user
MYSQL_PASSWORD = 'qwer1234'
MYSQL_DATABASE = 'lcm_db'  # 내가 생성한 db
connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string) #내 db에 정보를 넘겨줌
```

### API 호출 및 가공

```
import requests

url = "http://openapi.seoul.go.kr:8088/개인키/xml/TbCorona19CountStatusJCG/1/5/" #xml -> json 변경 가능.

rows=['JONGNOADD', 'JUNGGUADD', 'YONGSANADD', 'GWANGJINADD', 'DDMADD', 'JUNGNANGADD', 'SEONGBUKADD', 'GANGBUKADD', 'DOBONGADD', 'NOWONADD','EPADD','SDMADD','MAPOADD','YANGCHEONADD','GANGSEOADD','GUROADD','GEUMCHEONADD','YDPADD','DONGJAKADD','GWANAKADD','SEOCHOADD','GANGNAMADD','SONGPAADD','GANGDONGADD', 'ETCADD'] #호출 된 API에서 지역구 일일 확진자.
columns = ['JONGNO', 'JUNGGU', 'YONGSAN', 'GWANGJIN', 'DDM', 'JUNGNANG', 'SEONGBUK', 'GANGBUK', 'DOBONG', 'NOWON','EP','SDM','MAPO','YANGCHEON','GANGSEO','GURO','GEUMCHEON','YDP','DONGJAK','GWANAK','SEOCHO','GANGNAM','SONGPA','GANGDONG', 'ETC'] #호출 된 API에서 지역구 전체 확진자.

req = requests.get(url).content #requests.get을 이용해서 url 호출
xmlObject = xmltodict.parse(req) #호출된 xml을 dict로 전환해서 저장.
dict_data = xmlObject['TbCorona19CountStatusJCG']['row'] #일일 확진자 확인.
df_conf = pd.DataFrame(dict_data) #뽑힌 정보를 기반으로 데이터 프레임 생성.
df_conf = pd.melt(df_conf,
                  id_vars=['JCG_DT'],
                  value_vars=rows,
                  value_name='con',
                  ignore_index=False)
# 생성된 데이터 프레임을 melt method를 이용해서 내부 구조를 재가공.
df_conf_1 = df_conf.astype(
    {'JCG_DT': 'datetime64', "con": "int"})
df_conf_1.to_sql(name='test10', con=db, if_exists = 'replace', index= False)
db.execute('ALTER TABLE test5 ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')
print("PK 칼럼 추가")
```

<img src="mdimages_AiLEE96/DB_con&input.PNG">

