from pyzabbix.api import ZabbixAPI

ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER '
ZABBIXAPIPASSWORD = 'PASSWORD'


print (f"URL = {ZABBIXURL} \n USER = {ZABBIXAPIUSER} \n PASSWORD = {ZABBIXAPIPASSWORD} \n ==================== \n")

# Create ZabbixAPI class instance
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)
result1 = zapi.host.get(monitored_hosts=1, output='extend')

# Get all disabled hosts
result2 = zapi.do_request('host.get',
                              {
                                  'filter': {'status': 1},
                                  'output': 'extend'
                              })

# Filter results
hostnames1 = [host['host'] for host in result1]
hostnames2 = [host['host'] for host in result2['result']]

print(f"Печатаем result1 \n Create ZabbixAPI class instance \n {result1} \n ")
print(f"Печатаем result2 \n all disabled hosts \n {result2} \n ")
print(f"Печатаем hostnames1 \n Filter results \n  {hostnames1} \n ")
print(f"Печатаем hostnames2 \n Filter results \n {hostnames2} \n ")
"""print(f"Печатаем hostnames3 \n Filter results \n {hostnames3} \n ")"""

print(f"Печатаем список узлов")
for host in zapi.host.get(output = ['hostid','host','name'],  selectInterfaces=['ip','port','dns']):
    print (host)


#Get List of available groups
print(f" \nПечатаем список групп:")
groups = zapi.hostgroup.get(output=['itemid','name'])
for group in groups:
        print (group['groupid'],group['name'])



#Get List of hosts in the group
print(f" \nПолучаем список хостов в группе с id 2")
hosts = zapi.host.get(groupids=2, output=['hostid','name'])
for host in hosts:
        print (host['hostid'],host['name'])

#Get List of items on the host
print(f" \nПолучаем список итемов с хоста 10268")
items = zapi.item.get(hostids=10268, output=['itemid','name'])
for item in items:
        print (item['itemid'],item['name'])

# Get a list of all issues (AKA tripped triggers)
triggers = zapi.trigger.get(only_true=1,
                            skipDependent=1,
                            monitored=1,
                            active=1,
                            output='extend',
                            expandDescription=1,
                            selectHosts=['host'],
                            )

# Do another query to find out which issues are Unacknowledged
unack_triggers = zapi.trigger.get(only_true=1,
                                  skipDependent=1,
                                  monitored=1,
                                  active=1,
                                  output='extend',
                                  expandDescription=1,
                                  selectHosts=['host'],
                                  withLastEventUnacknowledged=1,
                                  )
unack_trigger_ids = [t['triggerid'] for t in unack_triggers]
for t in triggers:
    t['unacknowledged'] = True if t['triggerid'] in unack_trigger_ids \
        else False

# Print a list containing only "tripped" triggers
print (f"\n печатаем тригеры")
for t in triggers:
    if int(t['value']) == 1:
        print("{0} - {1} {2}".format(t['hosts'][0]['host'],
                                     t['description'],
                                     '(Unack)' if t['unacknowledged'] else '')
              )
# Logout from Zabbix
zapi.user.logout()

