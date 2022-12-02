### crontab
```
yum install -y cronie
systemctl restart cronie
crontab -e # 빈 스크립트에서 어떤 행동을 수행할지 작성.
```

```
crontab -l # 작성한 내용 확인
```
<img src="mdimages_AiLEE96/crontab.PNG">