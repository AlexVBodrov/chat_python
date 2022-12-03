"""
4. Продолжаем работать над проектом «Мессенджер»:
a) Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него. Уместно использовать модуль subprocess).
b) Реализовать скрипт, запускающий указанное количество клиентских приложений.
"""
import subprocess

process = []

while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, => кол-во клиентов, x - закрыть все окна:')

    if action == 'q':
        break
    elif action == 's':
        process.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))
        while True:
            max_clients = 8
            try:
                num_clients = int(input(f'Введите кол-во клиентов(от 2 до {max_clients - 1}): '))
            except:
                print('ValueError: invalid literal for int() with base 10')
                continue
            if isinstance(num_clients, int) and 1 < num_clients < max_clients:
                for num in range(0, num_clients):
                        process.append(subprocess.Popen(f'python client.py -n client{num}', creationflags=subprocess.CREATE_NEW_CONSOLE))
                break
            else:
                print(f'Неверный ввод. Введите кол-во клиентов(от 2 до {max_clients - 1})')
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()