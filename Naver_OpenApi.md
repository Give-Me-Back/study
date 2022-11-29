
# 네이버 Open Api 호출 소스

```
# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
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