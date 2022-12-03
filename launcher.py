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
        for num in range(0, int(input('Введите кол-во клиентов'))):
            process.append(subprocess.Popen(f'python client.py -n client{num}', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        while process:
            victim = process.pop()
            victim.kill()