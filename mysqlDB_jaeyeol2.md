# MysqlDB 설치
```
systemctl stop firewalld
systemctl disable firewalld
setenforce 0

yum install -y mysql-server

systemctl enable mysqld
systemctl start mysqld
systemctl status mysqld
```

## 보안설정
```
mysql -u root -p
-- 엔터

mysql_secure_installation



---
Securing the MySQL server deployment.

Connecting to MySQL using a blank password.

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: [ N ]

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
Please set the password for root here.

New password: [ qwer1234 ]

Re-enter new password: [ qwer1234 ]

Estimated strength of the password: 50
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : [ y ]
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : [ y ]
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : [ y ]
Success.

By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : [ y ]
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : [ y ]
Success.
---
```
### -접속 안되면
```
mysql -u root -p
엔터접속 후

set global validate_password_policy=LOW;   [패스워드 권한설정]
```
## 외부접속 설정
```
CREATE DATABASE 이니셜_db;
CREATE USER '이니셜'@'%' IDENTIFIED BY 'DB 계정 패스워드';
GRANT ALL PRIVILEGES ON 이니셜_db.* TO '이니셜'@'%';
FLUSH PRIVILEGES;
EXIT;
```

## DB 및 테이블 생성 test
```
mysql -u root -p

use 이니셜_db;
CREATE TABLE student (sname VARCHAR(10), sage INT);

INSERT INTO student VALUES('kim',10);
INSERT INTO student VALUES('lee',20);
INSERT INTO student VALUES('park',30);
INSERT INTO student VALUES('sim',40);
```

## Mysql 명령어
```
SHOW DATABASES;           [데이터베이스 확인]
USE 이니셜_db;            [데이터베이스 사용]
SHOW TABLES;              [테이블 확인]
SELECT*FROM 테이블명;     [테이블의 모든데이터 확인]