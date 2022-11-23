# MongoDB 설치

## 레포지터리 생성
```
vi /etc/yum.repos.d/mongodb-org-6.0.repo

[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
```
## 설치 및 실행
```
sudo yum install -y mongodb-org

sudo systemctl restart mongod
```
## 확인
```
sudo systemctl status mongod
ctrl + c
```
## MongoDB 접속
```
mongosh
```
## DB / 컬렉션 생성
```
DB생성
use "test01"

Collection 생성
db.createCollection("test")

Collection 확인
show collections
```
![default][img]
[img]: image/Mongodb/1.PNG

## python 연동
### 외부접속 허용
```
vi /etc/mongod.conf
```
![default][img]
[img]: image/Mongodb/2.PNG