import logging
logger = logging.getLogger('server')
from common.variables import DEFAULT_PORT

# Дескриптор для описания порта:
class Port:
    def __set__(self, instance, value):
        # value - port number - 7777
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.')
            exit(1)
        # Если порт прошел проверку, добавляем его в список атрибутов экземпляра
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        # owner - <class '__main__.Server'>
        # name - port
        self.name = name

class Set_Port_or_Default_Port:
    def __set__(self, instance: object, value: int) -> None:
        if not 1023 < value < 65536:
            logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта {value}. Допустимы адреса с 1024 до 65535.\nБудет установлен порт по умолчанию: {DEFAULT_PORT} ')
            value = DEFAULT_PORT
            # добавляем порт в список атрибутов экземпляра
        instance.__dict__[self.name] = value
    
    def __set_name__(self, owner, name):
        self.name = name

