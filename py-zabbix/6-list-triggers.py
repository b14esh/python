from pyzabbix.api import ZabbixAPI

# Переменные
ZABBIXURL = 'http://URL/zabbix/'
ZABBIXAPIUSER = 'USER'
ZABBIXAPIPASSWORD = 'PASSWORD'

# Создаем инстанс zapi
# Будем применять для дальнейших операций
zapi = ZabbixAPI(url=ZABBIXURL, user=ZABBIXAPIUSER, password=ZABBIXAPIPASSWORD)

# Получить список всех проблем (триггеры сработали)
triggers = zapi.trigger.get(only_true=1,
                            skipDependent=1,
                            monitored=1,
                            active=1,
                            output='extend',
                            expandDescription=1,
                            selectHosts=['host'],
                            )

# Получить список какие проблемы не подтверждены.
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

# Распечатать список, содержащий только "сработавшие" триггеры
print (f"\n печатаем триггеры")
for t in triggers:
    if int(t['value']) == 1:
        print("{0} - {1} {2}".format(t['hosts'][0]['host'],
                                     t['description'],
                                     '(Unack)' if t['unacknowledged'] else '')
              )


# Завершаем подключения
zapi.user.logout()