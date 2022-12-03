"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.

Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом. 

В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
"""
def ip_address():
    # create a new ip address
    pass

def host_ping(host):
    
    pass



def host_ping(list_hosts: list) -> str:
    try:
        for host in list_hosts:
            if ping_host(host):
                print (f"{host} Узел доступен")
            else:
                print(f"{host} Узел недоступен")
    except ValueError:
        print('ValueError')
    
    