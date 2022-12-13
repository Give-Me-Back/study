
# 네이버 Open Api 호출 소스

```
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
```

```
client_id = "YOUR_CLIENT_ID" #네이버 OpenApi에서 받은 client_id
client_secret = "YOUR_CLIENT_SECRET" #네이버 OpenApi에서 받은 client_secret
encText = urllib.parse.quote("검색할 단어") # "코로나" 라고 검색하면 코로나관련 뉴스 데이터만 추출된다.
```
## 네이버 OpenApi 신청주소
```
https://developers.naver.com/main/
```
```
위 내용은 오픈소스이며
아래부터는 장고를 활용해 웹에 띄우기까지의 main.py의 소스
```
```
from PyNaver import Naver
from sqlalchemy import create_engine

client_id = "클라이언트 ID"
client_secret = "클라이언트 KEY"

url = "https://openapi.naver.com/v1/search/news.xml?query="

naver = Naver(client_id, client_secret)
query = "코로나 확진자" # 검색
display = '10' # 출력 수
sort = "sim"

df = naver.search_news(query=query, display=display, sort=sort)
df.head()
print(type(df))

MYSQL_HOSTNAME = '192.168.131.20:3306'  # 내 mysql ip
MYSQL_USER = 'test'  # 내가 생성한 user
MYSQL_PASSWORD = 'qwer1234'
MYSQL_DATABASE = 'test_db'   # 내가 생성한 db

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)

df = df.astype({"pubDate": "datetime64"}) # 날짜데이터 타입변경

df.to_sql(name='news', con=db, if_exists = 'replace', index= False)
# if_exists
# replace = 기존데이터 삭제후 새로운데이터 갱신
# append = 기존데이터 위에 덮어쓰기
db.execute('ALTER TABLE news ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')