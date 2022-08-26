# Создайте программу для игры в ""Крестики-нолики"".




from multiprocessing.resource_sharer import stop
import tracemalloc 


def print_field (list):
    a = 0
    print('_____________')
    for i in range (0,3):
        print('|', end=' ')
        for j in range (0,3):
            print(list[a], end=' | ')
            a+=1
        print('\n_____________')


def hod(name, list):
    a = int(input(f'Куда ставим {name}?  '))
    if list[a-1] != 'X' and list[a-1] != 'O':
        if name == 'крестик':
            list[a-1] = 'X'
        else: list[a-1] = 'O'
    else: 
        print('Неверный ход')
        hod(name, list)
    return list


def check(list):
    if list[0]==list[1]==list[2]: 
        if list[0]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[3]==list[4]==list[5]:
        if list[3]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[6]==list[7]==list[8]:
        if list[6]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[0]==list[3]==list[8]:
        if list[0]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[1]==list[4]==list[7]:
        if list[1]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[2]==list[5]==list[8]:
        if list[2]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[0]==list[4]==list[8]:
        if list[0]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик') 
        return True
    elif list[2]==list[4]==list[6]:
        if list[2]== 'X':
            print(f'побеждает крестик') 
        else: print(f'побеждает Нолик')  
        return True
    else: return False


name = ['крестик', 'нолик', 'крестик', 'нолик', 'крестик', 'нолик', 'крестик', 'нолик', 'крестик']
desk = [1,2,3,4,5,6,7,8,9]

print_field(desk)


for i in range (0, len(desk)):
    if check (desk,) == False:
        desk = hod(name[i], desk)
        print_field(desk)
    else: 
        print_field(desk)
        stop