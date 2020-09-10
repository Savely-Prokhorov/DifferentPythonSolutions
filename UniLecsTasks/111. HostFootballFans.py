fans_num1 = int(input('Введите кол-во болельщиков 1: '))
fans_num2 = int(input('Введите кол-во болельщиков 2: '))
places = int(input('Введите кол-во мест в номерах: '))

if fans_num1 % places == 0:
    rooms1 = fans_num1 // places
else:
    rooms1 = fans_num1 // places + 1

if fans_num2 % places == 0:
    rooms2 = fans_num2 // places
else:
    rooms2 = fans_num2 // places + 1

print(rooms1 + rooms2)
