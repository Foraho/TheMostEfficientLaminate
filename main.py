import pygame

width = 14
lenght = 138
count = 200
# длина и ширина комнаты в метрах
width_room, lenght_room = 2.84,10.2
whips = 46 # нахлёст, обычно не меньше 40см
lmt = [] # переменная для хранения целых кусков ламината
lmt_cut_D = [] # переменная для хранения порезаных кусков down
lmt_cut_U = [] # переменная для хранения порезаных кусков up
lmt_cut_trash = [] # переменная для хранения кусков которые уже никуда не использовать
point = [lenght_room * 10,width_room * 10] # хранение текущей точки от куда рисовать
attempts = round(lenght_room*100/width) # кол-во рядов ламината
attempts_lst = {} # словарь для хранения длины на каждой ширине комнаты
amogus = {} # хранит размеры обрезков
bebra = lenght # хранит длину текущего куска для использования нахлёста, а длина прошлого куска лежит в last_bebra
# установка размеров окна, цвета заденго фона и линий
pygame.init()
screen = pygame.display.set_mode((lenght_room * 120, width_room * 200))
YELLOW = (180,180,0)
RED = (180,0,0)


# рисование прямоугольников
def draw(x,y,xl,yl, rectangle_color = (110, 110, 110)):
    # rectangle_color = (255, 255, 255)
    rectangle = pygame.Rect(x, y, xl, yl)  # Установка координат и размеров прямоугольника
    pygame.draw.rect(screen, rectangle_color, rectangle, 1)  # Отрисовка прямоугольника на экране
    pygame.display.flip()  # Обновление экрана

class laminate:

    def __init__(self, lenght):
        self.lenght = lenght
        self.Up = True
        self.Down = True

    def cut(self, lenght, up=False, dowm=False): # lmt_cut_U - значит Up сторона целая; lmt_cut_D - значит Down сторона целая
        self.lenght-=lenght
        if up:
            self.Up=False
        if dowm:
            self.Down=False


# создание словаря, номер ряда:кол-во доступных см в нём
for i in range(attempts):
    attempts_lst[i] = width_room*100

for i in range(count):
    lmt.append(laminate(lenght))


for i in attempts_lst.keys():
    last_bebra = bebra
    amogus[lenght] = 1
    bebra = lenght
    if len(lmt_cut_U) > 0: # чекаем куск
        info = list(lmt_cut_U[0].__dict__.values())[0]
        if last_bebra-whips>=0:
            info=last_bebra-whips
            bebra = info
            draw(point[0], point[1], width, info)
            point[1] += info
            attempts_lst[i] -= info
            lmt_cut_trash.append(lmt_cut_U[0].lenght-info)
            lmt_cut_U.pop(0)
            if bebra==0: bebra = lenght
            else: amogus[info] = 1 # ВАРИАНТ 2


    while attempts_lst[i] - lenght > 0: # кладём целыые куски пока ширина позволяет
        draw(point[0], point[1], width, lenght) # рисуем ламинат
        attempts_lst[i]-=lenght # уменишение кол-во оставшегося растояния на текущий ряд
        point[1]+=lenght # увеличиваем координаты точки для рисования другого куска
        try: lmt.pop(0)
        except: print('!!!!!!\n!!!!!!\n!!! Не хВаТаЕт !!!\n!!!!!!\n!!!!!!'); exit()
    if len(lmt) > 0: # кладём обрезки
        # amogus[attempts_lst[i]] = 1  # ВАРИАНТ 1
        draw(point[0], point[1], width, attempts_lst[i])  # рисуем ламинат
        # режем ламинат, кладём, а остаток кладём в переменную lmt_cut_U
        lmt[0].cut(attempts_lst[i], dowm=True)
        lmt_cut_U.append(lmt[0])
        lmt.pop(0)
        attempts_lst[i] = 0  # делаем оставшуюся свободное расстояние в текущем ряду на 0 (что озночает ряд закончен)
    # перенос координат точки для рисования на новый ряд
    point[0] += width
    point[1] = width_room * 10

# рисуем комнату
draw(lenght_room * 10, width_room * 10, lenght_room * 100, width_room * 100, rectangle_color = (150, 150, 150))

print(f'\nдлины мусорных отрезков {lmt_cut_trash}')
print('/////U/////')
for item in lmt_cut_U:
    print(item.lenght)
print('/////D/////')
for item in lmt_cut_D:
    print(item.lenght)


f1 = pygame.font.Font(None, 36)
text1 = f1.render(str(list(set(amogus.keys()))), 1, (180, 180, 0))
screen.blit(text1, (lenght_room * 10, width_room * 130))
text1 = f1.render(f'{len(lmt)} кусков оказались лишними, кол-во обрезков U: {len(lmt_cut_U)} и D: {len(lmt_cut_D)}; мусора {len(lmt_cut_trash)}', 1, YELLOW)
screen.blit(text1, (lenght_room * 10, width_room * 150))
if sum(attempts_lst.values()) != 0:
    text1 = f1.render(
    f'не хватило ~ {sum(attempts_lst.values())} см',1, RED)
    screen.blit(text1, (lenght_room * 10, width_room * 170))
pygame.display.update()


# Ожидание закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(1000)