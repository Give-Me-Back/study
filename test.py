import requests

url = 'http://apis.data.go.kr/1790387/covid19CurrentStatusHospitalizations/'
params ={'serviceKey' : 'mzjIzYfhSW5dqdJTPqPf3RJs2SStFPYtduOgTIRFz28fZZ8iHByfnxVaEtoqiErdfjS0Mo60WUCWNWks9Z3OwQ%3D%3D' }

response = requests.get(url, params=params)
print(response.content)