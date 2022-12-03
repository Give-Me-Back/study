# CentOs8에서 Python3.10 버전대 설치
## Python 필수 구성요소 설치
```
sudo dnf install wget yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel 
```
## Python3.10 압축파일 다운 및 압축해제
```
wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz

tar xzf Python-3.10.8.tgz 
```
## 디렉토리를 Python-3.10.8로 이동 및 컴파일하기 전에 필요한 값으로 소스코드 준비
```
cd Python-3.10.8

sudo ./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions 
```
## make로 소스 코드 컴파일
```
sudo make -j ${nproc}

sudo make altinstall
```
## 아카이브 파일 삭제
```
sudo rm Python-3.10.8.tgz
```
## 파이썬 버전 확인
```
python3.10 -V

파이썬 3.10.8
```
## PIP 버전확인
```
pip3.10 -V  

/usr/local/lib/python3.10/site-packages/pip(파이썬 3.10)의 pip 20.2.3
```
## 파이썬 가상 환경 만들기
```
cd ~/python-app/ 
sudo /usr/local/bin/python3.10 -m venv appenv
```
## 가상환경 활성화
```
source appenv/bin/activate
```
## 가상환경 나가기
```
deactivate
```