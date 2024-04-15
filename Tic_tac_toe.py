board = list(range(1, 10))

player_x = "X"
player_o = "O"


def show_board():
    for i in range(3):
        print(f'', board[i*3], '|', board[i*3+1], '|', board[i*3+2])
        if i < 2:
            print('---+---+--')


def win_check():
    win = False
    win_comb = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    )

    for i in win_comb:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]]:
            win = True

    return win


def is_busy(position, player):
    if position > 9 or position < 1:
        print('Вы ввели неверное число, попробуйте снова.')
        show_board()
        play(player)
    elif board[position-1] in [player_o, player_x]:
        print('Упс, здесь уже занятая клетка, выберите другую.')
        show_board()
        play(player)
    else:
        return True


def play(player):
    check_position = int(input(f'Ход игрока за {player} выберите номер клетки от 1 до 9:'))

    if is_busy(check_position, player):
        board.pop(check_position - 1)
        board.insert(check_position - 1, player)


def play_game():
    current_player = player_x
    turn = 1

    while turn < 10:
        show_board()
        play(current_player)

        if win_check():
            if current_player == player_x:
                winner = 'Крестики'
            else:
                winner = 'Нолики'
            show_board()
            print(f'{winner} победили!')
            break

        turn += 1
        if current_player == player_x:
            current_player = player_o
        else:
            current_player = player_x
    if turn == 10:
        show_board()
        print('К сожалению у вас ничья!')


play_game()
