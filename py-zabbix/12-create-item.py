from pyzabbix.api import ZabbixAPI, ZabbixAPIException
import sys

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

#Печатаем все группы узлов
print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])

#Получаем список хостов в группе 5
print(f" \nПолучаем список хостов в группе с id 5:")
hosts = zapi.host.get(groupids=5, output=['hostid','name'])
for host in hosts:
        print (host['hostid'],host['name'])



host_name = 'blablalbalba3'

hosts = zapi.host.get(filter={"host": host_name}, selectInterfaces=["interfaceid"])
if hosts:
    host_id = hosts[0]["hostid"]
    print("\nНайден host id {0}".format(host_id))

    try:
        item = zapi.item.create(
            hostid=host_id,
            name='Used disk space on $1 in %',
            key_='vfs.fs.size[/,pused]',
            type=0,
            value_type=3,
            interfaceid=hosts[0]["interfaces"][0]["interfaceid"],
            delay=30
        )

    except ZabbixAPIException as e:
        print(e)
        sys.exit()

    print("Добавили item для itemid {0} на host: {1}".format(item["itemids"][0], host_name))
else:
    print(f"\nХост {host_name} не обнаружен.")



# Завершаем подключения
zapi.user.logout()