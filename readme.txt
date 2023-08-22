rus:

!!! БАГИ !!!
- * variable count * - указывайте значение хотя бы немного больше чем надо, например если необходимо ровно 100 кусков ламината то укажите 150, код всё равно выведет сколько кусков лишние, иначе при значениях ±98,±99 или то что около того он не скажет что кусков не хватает
- * attempts_list.values() * когда код выводит кол-во см которое не хватило то то количество которое он выводит это лишь примерное значение, в реальности прибовляйте к этому заначению 10-30%, либо просто введите больше кусков ламината, всё равно код покажет если остануться лишние куски


==================================================================


width - ширина ламината
lenght - длина ламината
count - количество ламината

width_room - расстояние ↑↓ на экране
length_room - расстояние == на экране

whips - перекрытие, расстояние между ламинатом

lmt - переменная для хранения целых кусков ламината
lmt_cut_D - переменная для хранения отрезанных кусков вниз
lmt_cut_U - переменная для хранения отрезанных кусков вверх
lmt_cut_trash - переменная для хранения кусков, которые больше нигде не используются

point - хранение текущей точки от куда рисовать
attempts - кол-во рядов ламината
attempts_lst - словарь для хранения длины на каждой ширине комнаты
amogus - хранит размеры обрезков
bebra - хранит длину текущего куска для использования нахлёста, а длина прошлого куска лежит в last_bebra






eng:

!!! BUGS !!!
- * variable count* - specify the value at least a little more than necessary, for example, if you need exactly 100 pieces of laminate, then specify 150, the code will still output how many extra pieces, otherwise at values ± 98, ± 99 or something like that, it will not say that there are not enough pieces
- * attempts_list.values() * when the code outputs the number of cm that was not enough, the amount that it outputs is only an approximate value, in reality, add 10-30% to this stash, or simply enter more pieces of laminate, the code will still show if there are extra pieces left



==================================================================


width - width of laminate
lenght - length of laminate
count - count of laminate

width_room - distance of ↑↓ on screen
lenght_room - distance ←→ on screen

whips - overlap, distance between laminate

lmt - variable for storing whole pieces of laminate
lmt_cut_D - variable for storing cut pieces down
lmt_cut_U - variable for storing cut pieces up
lmt_cut_trash - variable for storing pieces that are no longer used anywhere

point - storing the current point from where to draw
attempts - number of rows of laminate
attempts_lst - dictionary for storing length on each width of the room
among us - stores the sizes of clippings

bebra - stores the length of the current chunk to use overlap, and the length of the last chunk lies in last_bebra