import dis

class ClientVerifier(type):
    """
    Проверяет отсутствие вызовов accept и listen для сокетов;
    использование сокетов для работы по TCP;
    отсутствие создания сокетов на уровне классов
    """
    def __init__(self, clsname, bases, clsdict):
        list_methods = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы.
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in list_methods:
                            list_methods.append(i.argval)
        # Если обнаружено использование недопустимого метода accept, listen, socket бросаем исключение:
        for command in ('accept', 'listen', 'socket'):
            if command in list_methods:
                raise TypeError('В классе обнаружено использование запрещённого метода')
        # Вызов get_message или send_message из utils считаем корректным использованием сокетов
        if 'get_message' in list_methods or 'send_message' in list_methods:
            pass
        else:
            raise TypeError('Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(clsname, bases, clsdict)


class ServerVerifier(type):
    """
        выполняет базовую проверку класса Server;
        отсутствие вызовов connect для сокетов;
        использование сокетов для работы по TCP. 
    """
    def __init__(self, clsname, bases, clsdict):
        list_methods = []
        list_attrs = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in list_methods:
                            # заполняем список методами, использующимися в функциях класса
                            list_methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in list_attrs:
                            # заполняем список атрибутами, использующимися в функциях класса
                            list_attrs.append(i.argval)
        # Если обнаружено использование connect, бросаем исключение:
        if 'connect' in list_methods:
            raise TypeError('Использование метода connect недопустимо в серверном классе')
        # Если сокет не инициализировался константами SOCK_STREAM(TCP) AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in list_attrs and 'AF_INET' in list_attrs):
            raise TypeError('Некорректная инициализация сокета.')
        super().__init__(clsname, bases, clsdict)