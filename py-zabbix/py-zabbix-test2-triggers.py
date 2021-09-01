# https://www.zabbix.com/documentation/current/ru/manual/api
from datetime import datetime
from pyzabbix.api import ZabbixAPI

ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'


print (f"URL = {ZABBIXURL} \n USER = {ZABBIXAPIUSER} \n PASSWORD = {ZABBIXAPIPASSWORD} \n ==================== \n")

# Create ZabbixAPI class instance
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Get List of available groups
print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])

# Get a list trigges groupids=2
triggers = zapi.trigger.get(groupids=2, output='extend', expandDescription=1, selectHosts=['host'],)

# Print all trigges group 2
#print(f"\n Печатаем все тригеры groupids2 {triggers}")

print("\n")

for t in triggers:
    print("{0} - {1} - {2}".format(t['hosts'][0]['host'], t['description'], datetime.utcfromtimestamp(int(t['lastchange'])).strftime('%Y-%m-%d %H:%M:%S')))

# Logout from Zabbix
zapi.user.logout()

