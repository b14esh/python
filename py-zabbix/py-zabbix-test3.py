# https://www.zabbix.com/documentation/current/ru/manual/api
from datetime import datetime
from pyzabbix.api import ZabbixAPI

ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


#print (f"\n ==================== \n URL = {ZABBIXURL} \n USER = {ZABBIXAPIUSER} \n PASSWORD = {ZABBIXAPIPASSWORD} \n ==================== \n")

# Create ZabbixAPI class instance
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Get List of available groups
#print(f" \nПечатаем список групп:")
#groups = zapi.hostgroup.get(output=['itemid','name'])
#for group in groups:
#        print (group['groupid'],group['name'])

#Get a list trigges groupids=2
#triggers = zapi.trigger.get(host="hsrv1_factoria", output='extend', expandDescription=1,  expandExpression=1, selectHosts=['host'],)

#Print all trigges group 2
#print(f"\n Печатаем все тригеры groupids2 \n {triggers}")


#print(f"Печатаем список узлов:")
#for host in zapi.host.get(output = ['hostid','host','name'],  selectInterfaces=['ip','port','dns']):
#    print (host)


#for t in triggers:
#   print("{0} - {1} - {2}".format(t['hosts'][0]['host'], t['description'], datetime.utcfromtimestamp(int(t['lastchange'])).strftime('%Y-%m-%d %H:%M:%S')))
   #print("{0} - {1} - {2}".format(t['hosts'][0]['host'], t['description'],t['lastchange'], ))


problem = zapi.problem.get(host='hsrv1_factoria', recent='true')

##print("\n", problem)
for pr in problem:
   print("{0} - {1} - {2} ".format(pr['eventid'], pr['name'], pr['clock']))



### Бля
### из доков Для получения проблем, которые были решены ранее, используйте event.get метод.


event.get(объект параметры)




# Logout from Zabbix
zapi.user.logout()
