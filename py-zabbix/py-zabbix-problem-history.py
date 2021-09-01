# https://www.zabbix.com/documentation/current/ru/manual/api
from datetime import datetime
from pyzabbix.api import ZabbixAPI
import csv
from contextlib import redirect_stdout

ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


#print (f"\n ==================== \n URL = {ZABBIXURL} \n USER = {ZABBIXAPIUSER} \n PASSWORD = {ZABBIXAPIPASSWORD} \n ==================== \n")

# Параметры подключения к zabbix API
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#print(f" \nПечатаем список групп:")
#groups = zapi.hostgroup.get(output=['itemid','name'])
#for group in groups:
#        print (group['groupid'],group['name'])


#print(f"Печатаем список узлов:")
#for host in zapi.host.get(output = ['hostid','host','name'],  selectInterfaces=['ip','port','dns']):
#    print (host)

#Zabbix ведет время от создания linux
#Для уточнения времени исполняем стандартую команду linux
#date -d @1620925819
problem = zapi.event.get(groupids=2,time_from=1620925819)

## Может пригодится для уточнения обьектов
##print("\n", problem)

# Печатаем проблемы
#for pr in problem:
    #print("{0} - {1} - {2} ".format(pr['eventid'], pr['name'], pr['clock']))
#    print("{0} - {1} - {2} ".format(pr['eventid'], pr['name'], datetime.utcfromtimestamp(int(pr['clock'])).strftime('%Y-%m-%d %H:%M:%S')))

#Запись CSV файла
with open('out.csv', 'w', encoding='utf_8') as f:
    with redirect_stdout(f):
        for pr in problem:
            print("{0};{1};{2} ".format(pr['eventid'], pr['name'], datetime.utcfromtimestamp(int(pr['clock'])).strftime('%Y-%m-%d %H:%M:%S')))

# Logout from Zabbix
zapi.user.logout()
