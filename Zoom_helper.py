import webbrowser
import pyglet
import datetime
import time
import os

os.system('CLS')
print('Zoom helper\n░█████╗░██████╗░███████╗░█████╗░████████╗███████╗██████╗░  ██████╗░██╗░░░██╗  ████████╗███████╗███╗░░░███╗░█████╗░\n██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝  ╚══██╔══╝██╔════╝████╗░████║██╔══██╗\n██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░  ░░░██║░░░█████╗░░██╔████╔██║███████║\n██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░  ░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║\n╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗██████╔╝  ██████╦╝░░░██║░░░  ░░░██║░░░███████╗██║░╚═╝░██║██║░░██║\n░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝')


def playsound():
    sound = pyglet.media.load('music.mp3')
    sound.play()
    pyglet.app.run()


x = 0
print('Введите время урока')
time_hour = int(input('>> '))
time_minute = int(input('>> '))
now = datetime.datetime.now()
hour = time_hour - now.hour
if hour < 0:
    hour += 24
    x = 1
minute = time_minute - now.minute
if minute < 0:
    minute += 60
    x = 1
if x != 1:
    print('Урок начнется через ', hour,
          ' часов и ', minute, ' минут')
    print('')
else:
    print('Урок уже идёт')
zoom = input('Вставьте ссылку на урок\n>> ')

a = 0
if now.hour >= time_hour and now.minute >= time_minute:
    print('*Открываю zoom*')
    webbrowser.open(zoom, new=2)
    a = 1
    time.sleep(0)

while True:
    if a == 1:
        break
    time.sleep(0.5)
    os.system('CLS')
    print('W')
    time.sleep(0.5)
    os.system('CLS')
    print('WA')
    time.sleep(0.5)
    os.system('CLS')
    print('WAI')
    time.sleep(0.5)
    os.system('CLS')
    print('WAIT')
    time.sleep(0.5)
    os.system('CLS')
    print('WAI')
    time.sleep(0.5)
    os.system('CLS')
    print('WA')
    time.sleep(0.5)
    os.system('CLS')
    now = datetime.datetime.now()
    if now.hour == time_hour and now.minute == time_minute:
        print('!ДЛЯ ОТКЛЮЧЕНИЯ МУЗЫКИ ЗАКРОЙТЕ ПРОГРАММУ!')
        print('*Открываю zoom*')
        webbrowser.open(zoom, new=2)
        print('*Включаю трек*')
        playsound()
        break
