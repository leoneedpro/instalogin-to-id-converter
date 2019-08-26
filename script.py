# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# ИМПОРТ МОДУЛЕЙ
# ------------------------------------------------------------------
import requests
import json
# ------------------------------------------------------------------
# # ОБЪЯВЛЕНИЕ ПЕРЕМЕННЫХ
# ------------------------------------------------------------------
session = requests.Session()

#logins = open("logins.txt","r").read().split() # загрузка из файла

logins = ['apple', 'microsoft', 'instagrasasdasd2m'] # список/массив логинов
ids = ['5821462185', '524549267', '250253202232'] # список/массив id
# ------------------------------------------------------------------
# # Username to ID
# ------------------------------------------------------------------
if len(logins) != 0:
    print('------------------')
    print('ID - аккаунтов')
    print('------------------')
for i in range(len(logins)):
	try:
		response = session.get('https://instagram.com/'+logins[i]+'?__a=1')
		data = json.loads(response.text)
		id = data['graphql']['user']['id']
		file = open("out logins.txt","a+") # запись в текст
		out = file.write(id + "\n")
		file.close()
		print(id)
	except json.decoder.JSONDecodeError: # если аккаунт не найден, продолжаем работу
		continue
# ------------------------------------------------------------------
# # ID to Username
# ------------------------------------------------------------------
if len(ids) != 0:
    print('------------------')
    print('Username - аккаунтов')
    print('------------------')
for i in range(len(ids)):
	try:
		response = session.get('https://i.instagram.com/api/v1/users/'+ids[i]+'/info/')
		data = json.loads(response.text)
		id = data['user']['username']
		file = open("out logins.txt","a+")
		out = file.write(id + "\n")
		file.close()
		print(id)
	except json.decoder.JSONDecodeError:
		continue
