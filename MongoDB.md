# MongoDB 설치

## 레포지터리 생성

vi /etc/yum.repos.d/mongodb-org-6.0.repo

<pre>
<code>
vi /etc/yum.repos.d/mongodb-org-6.0.repo

[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
</pre>
</code>

## 설치
```
sudo yum install -y mongodb-org

sudo systemctl restart mongod
```

## 실행
```
mongosh
```
