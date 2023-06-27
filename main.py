import pygame
# хлёст мин 40см
# длина, ширина и кол-во ламината
width = 14
lenght = 138
count = 117
# длина и ширина комнаты в метрах
width_room, lenght_room = 2.8,10.2
lmt = [] # переменная для хранения целых кусков ламината
lmt_cut_D = [] # переменная для хранения порезаных кусков down
lmt_cut_U = [] # переменная для хранения порезаных кусков up
point = [lenght_room * 10,width_room * 10] # хранение текущей точки от куда рисовать
attempts = round(lenght_room*100/width) # кол-во рядов ламината
attempts_lst = {} # словарь для хранения длины на каждой ширине комнаты
amogus = {} # хранит размеры обрезков
# установка размеров окна, цвета заденго фона и линий
pygame.init()
screen = pygame.display.set_mode((lenght_room * 120, width_room * 200))


# рисование прямоугольников
def draw(x,y,xl,yl, rectangle_color = (255, 255, 255)):
    background_color = (255, 255, 255)
    # rectangle_color = (255, 255, 255)
    rectangle = pygame.Rect(x, y, xl, yl)  # Установка координат и размеров прямоугольника
    pygame.draw.rect(screen, rectangle_color, rectangle, 1)  # Отрисовка прямоугольника на экране
    pygame.display.flip()  # Обновление экрана

# --- отладка ---
# pygame.draw.circle(screen, rectangle_color, point, 3)

class laminate:

    def __init__(self, lenght):
        self.lenght = lenght
        self.Up = True
        self.Down = True

    def cut(self, lenght, up=False, dowm=False):
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

# рисуем комнату
draw(lenght_room * 10, width_room * 10, lenght_room * 100, width_room * 100)


print(f'd {len(lmt_cut_U)}, u {len(lmt_cut_D)}, lmt {len(lmt)}')
for i in attempts_lst.keys():
    if len(lmt_cut_U) > 0: # чекаем куски
        info = list(lmt_cut_U[0].__dict__.values())[0]
        draw(point[0], point[1], width, info)
        point[1] += info
        attempts_lst[i] -= info
        lmt_cut_U.pop(0)
    while attempts_lst[i] - lenght > 0: # кладём целыые куски пока ширина позволяет
        if len(lmt) == 0:
            print('Ламинат кончился, на всю комнату его не хватило', attempts*lenght, ' см')
            break
        draw(point[0], point[1], width, lenght) # рисуем ламинат
        attempts_lst[i]-=lenght # уменишение кол-во оставшегося растояния на текущий ряд
        point[1]+=lenght # увеличиваем координаты точки для рисования другого куска
        lmt.pop(0) # удаляем первый кусок так как мы его только что положили
    if len(lmt) > 0: # кладём обрезки
        amogus[attempts_lst[i]] = 1
        draw(point[0], point[1], width, attempts_lst[i])  # рисуем ламинат
        # режем ламинат, кладём, а остаток кладём в переменную lmt_cut_U
        lmt[0].cut(attempts_lst[i], dowm=True)
        lmt_cut_U.append(lmt[0])
        lmt.pop(0)
        attempts_lst[i] = 0  # делаем оставшуюся свободное расстояние в текущем ряду на 0 (что озночает ряд закончен)
    # перенос координат точки для рисования на новый ряд
    point[0] += width
    point[1] = width_room * 10

for i in amogus.keys():
    print(i)
print(f'{len(lmt)} кусков оказались лишними, кол-во обрезков {len(lmt_cut_U)}')

# Ожидание закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.time.delay(1000)