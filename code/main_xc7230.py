from pymongo import MongoClient
import requests
import pandas as pd
import xmltodict
import pymysql
from sqlalchemy import create_engine
from datetime import datetime, timedelta

### mysql 연결
MYSQL_HOSTNAME = '192.168.197.80:3306'  # 내 mysql ip
MYSQL_USER = 'kjh'  # 내가 생성한 user
MYSQL_PASSWORD = 'qwer1234'
MYSQL_DATABASE = 'kjh_db'   # 내가 생성한 db

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)   # 내 db와 연결

url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api'

gubun = ['검역', '전북', '충북', '강원', '제주', '합계', '대구', '경북', '서울', '인천', '경남', '세종', '대전', '경기', '광주', '울산', '부산', '전남', '충남']

# API 데이터 입력
def api_to_mysql():
    for i in gubun:
        params = {'serviceKey': '시크릿키',
                  'apiType': 'xml',
                  'gubun': f"{i}" }
        req = requests.get(url, params=params).content
        xmlObject = xmltodict.parse(req)
        dict_data = xmlObject['response']['body']['items']['item']
        df_conf = pd.DataFrame(dict_data)
        df_conf = df_conf.drop_duplicates(['gubun', 'stdDay'])
        df_conf_1 = df_conf.astype(
            {'deathCnt': 'int', "isolClearCnt": "int",
             "localOccCnt": "int", "overFlowCnt": "int", "stdDay": "datetime64"})
        print(i)
        df_conf_1.to_sql(name='test', con=db, if_exists = 'append', index= False)
    # 테이블에 PK칼럼 추가
    db.execute('ALTER TABLE test4 ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')
    print("PK 칼럼 추가")


# 최신데이더 추가
def new_data():
    new_data = datetime.now().date() - timedelta(1)
    params = {'serviceKey': '시크릿키',
              'apiType': 'xml',
              'std_day': f"{new_data}" }
    req = requests.get(url, params=params).content
    xmlObject = xmltodict.parse(req)
    dict_data = xmlObject['response']['body']['items']['item']
    df_conf = pd.DataFrame(dict_data)
    df_conf = df_conf.drop_duplicates(['gubun', 'stdDay'])
    df_conf_1 = df_conf.astype(
        {'deathCnt': 'int', "isolClearCnt": "int",
         "localOccCnt": "int", "overFlowCnt": "int", "stdDay": "datetime64"})
    df_conf_1.to_sql(name='test', con=db, if_exists='append', index=False)
    print(df_conf_1)
    print("데이터갱신")
