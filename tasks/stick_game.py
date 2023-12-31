# А теперь первое серьёзное домашнее задание. Вы попробуете разработать игру.

# Предлагаю древнюю китайскую игру в палочки.

# Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек. 
# Играют до тех пор пока не закончатся палочки. Тот кто взял последним - тот проиграл.

# Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек. 
# На каждом ходу выводите на консоль текущее количество оставшихся палочек и просите ввести количество палочек, 
# которое хочет взять игрок (который делает ход). Не забывайте менять очерёдность игроков и сокращать кол-во палочек. 
# В конце надо вывести кто победил - первый или второй игрок.

# Нюансы реализации могут отличаться. Кто-то может захотет запросить имена у игроков. Кто-то может захотеть реализовать не с 10-ю палочками, 
# а с тем количеством, которое введёт пользователь (может он хочет играть с 20-ю палочками?).

#Необходимо сделать на уровне функции

number_of_sticks = 10
player_turn = 1

while number_of_sticks > 0:
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks')
        continue
    
    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if number_of_sticks <= 0:
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost!')

    player_turn = 1 if player_turn == 2 else 2