import webbrowser
import pyglet
import datetime
import time
import os

os.system('CLS')
print('░█████╗░██████╗░███████╗░█████╗░████████╗███████╗██████╗░  ██████╗░██╗░░░██╗  ████████╗███████╗███╗░░░███╗░█████╗░\n██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝  ╚══██╔══╝██╔════╝████╗░████║██╔══██╗\n██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░  ░░░██║░░░█████╗░░██╔████╔██║███████║\n██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░  ░░░██║░░░██╔══╝░░██║╚██╔╝██║██╔══██║\n╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗██████╔╝  ██████╦╝░░░██║░░░  ░░░██║░░░███████╗██║░╚═╝░██║██║░░██║\n░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝')


def playsound():
    sound = pyglet.media.load('music.mp3')
    sound.play()
    pyglet.app.run()


print('Введите время урока')
time_hour = int(input('>> '))
time_minute = int(input('>> '))
now = datetime.datetime.now()
minute = time_minute - now.minute
if minute < 0:
    minute += 60
print('Урок начнется через ', time_hour - now.hour,
      ' часов и ', minute, ' минут')
print('')

xim = "https://us04web.zoom.us/j/2040326923?pwd=eTljOTNINTVTMjhIOFF1bGtiQnZ5Zz09"
fiz = "https://us04web.zoom.us/j/5881973664?pwd=ZGNSRmdSTW8rVFRnajRWb2tWZ2tYUT09"
inf_shishkin = "https://us05web.zoom.us/j/9533191569?pwd=cEY0Y2MwS1FpeVc3SlZJcmkwR2pHdz09"
inf_shakyrov = "https://us04web.zoom.us/j/6791449129?pwd=V3hWTnFqdUZGMWYyY3VwaEpFODZHdz09"
bio = "https://us04web.zoom.us/j/7842344578?pwd=ZVNRZEFCMFRtYjJydXA3Y3NkaTMvZz09"
mat = "https://us04web.zoom.us/j/79506541821?pwd=MDNyZFNHR01rbGw1YkhhN09Pd1BkUT09"
rys = "https://us04web.zoom.us/j/79404837832?pwd=K09DQ01vM0c1RHdzOFl3R0JUS1dpdz09"
angl_volkova = "https://us04web.zoom.us/j/5802938865?pwd=S0E4YlJRSG1UYURNRWN0eGFVb2ZGZz09"
angl_tashbylatova = "https://us04web.zoom.us/j/3138197239?pwd=b2Y5eE9MUDhRN2k0U0E4SDIzeG8zQT09"
bask_atnabaeva = "https://us04web.zoom.us/j/78498462452?pwd=buQ-CpO8J-lkLL6CjugNxD9z-RDyAp.1"
fizra_m = "https://us04web.zoom.us/j/4239733183?pwd=clZMSWhHYSt4d3gySExTMWpZWDU2Zz09"
ist = "https://yandex.ru/search/?text=%D0%BF%D0%BE%D1%84%D0%B8%D0%BA%D1%88%D1%83+%D0%BA+%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%BC%D1%83+%D1%83%D1%80%D0%BE%D0%BA%D1%83+%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%B8%2F%D0%BE%D0%B1%D1%89%D0%B0%D0%B3%D0%B8&lr=172"
print('Введите либо название предмета (регистр не важен), либо его номер')
print('Химия = 1\nФизика = 2\nИнформатика = 3\nБиология = 4\nАлгебра / Геометрия = 5\nРусский = 6\nАнглийский = 7\nБашкирский = 8\nФизра(м) = 9\nИстория = 10')

yrok = input('>> ')
if yrok == 'Химия' or yrok == 'химия' or yrok == '1':
    zoom = xim
elif yrok == 'Физика' or yrok == 'физика' or yrok == '2':
    zoom = fiz
elif yrok == 'Информатика' or yrok == 'информатика' or yrok == '3':
    print('Тут надо ввести цифру')
    inf = int(input('Кто учитель?\nШишкин(1) / Шакуров(2)\n>> '))
    if inf == 1:
        zoom = inf_shishkin
    elif inf == 2:
        zoom = inf_shakyrov
elif yrok == 'Биология' or yrok == 'биология' or yrok == '4':
    zoom = bio
elif yrok == 'Алгебра' or yrok == 'Геометрия' or yrok == 'алгебра' or yrok == 'геометрия' or yrok == '5':
    zoom = mat
elif yrok == 'Русский' or yrok == 'русский' or yrok == 'Литература' or yrok == 'литература' or yrok == '6':
    zoom = rys
elif yrok == 'Английский' or yrok == 'английский' or yrok == '7':
    print('Тут надо ввести только цифру')
    angl = int(input('Кто учитель?\nВолкова(1) / Ташбулатова(2)\n>> '))
    if angl == 1:
        zoom = angl_volkova
    elif angl == 2:
        zoom = angl_tashbylatova
elif yrok == 'Башкирский' or yrok == 'башкирский' or yrok == '8':
    zoom = bask_atnabaeva
elif yrok == 'Физра' or yrok == 'физра' or yrok == '9':
    zoom = fizra_m
elif yrok == 'История' or yrok == 'история' or yrok == 'Общество' or yrok == 'общество':
    zoom = ist


while True:
    now = datetime.datetime.now()
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
    if now.hour == time_hour and now.minute == time_minute:
        print('!ДЛЯ ОТКЛЮЧЕНИЯ МУЗЫКИ ЗАКРОЙТЕ ПРОГРАММУ!')
        print('*Открываю zoom*')
        webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser(
            'C:\Program Files\Google\Chrome\Application\chrome.exe'))
        webbrowser.get('Chrome').open_new_tab(zoom)
        print('*Включаю трек*')
        break
playsound()
