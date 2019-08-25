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
logins = ['apple', 'microsoft', 'instagram'] # список/массив логинов
ids = ['5821462185', '524549267', '25025320'] # список/массив id
# ------------------------------------------------------------------
# # Username to ID
# ------------------------------------------------------------------
if len(logins) != 0:
    print('------------------')
    print('ID - аккаунтов')
    print('------------------')
   
    for i in range(len(logins)):
        try: # ОБРАБАТЫВАЕМ ОШИБКУ, И ПРОДОЛЖАЕМ РАБОТУ, ЕСЛИ ЛОГИН НЕ СУЩЕСТВУЕТ
            response = session.get('https://instagram.com/'+logins[i]+'?__a=1')
            data = json.loads(response.text)
            id = data['graphql']['user']['id']
            file1 = open("123.txt","a+") # ВЫВОД В TXT ФАЙЛ
		    file1.write(id + "\n")
		    file1.close()
            print(id)
        except json.decoder.JSONDecodeError:
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
            file1 = open("123.txt","a+") 
		    file1.write(id + "\n")
		    file1.close()
            print(id)
        except json.decoder.JSONDecodeError:
            continue
