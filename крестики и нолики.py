import pygame as pg

WIDTH = 900
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

FPS = 60
CLOCK = pg.time.Clock()
WIN_COMBINATIONS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # горизонтальные линии
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # вертикальные линии
    (0, 4, 8), (2, 4, 6)  # диагональные линии

)


def main():
    # звуки
    pg.mixer.init()
    click_sound = pg.mixer.Sound("tic tac toe/ScreenRecorderProject1.mp3")
    click_sound.set_volume(0.4)
    start_music()

    # экран и задний фон
    screen = pg.display.set_mode(SIZE)
    # background = pg.image.load("history.png")
    # background = pg.transform.scale(background, SIZE)

    # создаем квадраты доски
    board = get_board()

    # содержимое
    contents: list[str | None] = [None for _ in range(9)]

    winner = mainloop(screen, board, contents, click_sound)

    draw(screen, board, contents )
    win_screen(winner, screen)


def draw(screen: pg.Surface, board, contents):
    # r = randint(0,255)
    screen.fill(pg.Color(255, 191, 229))
    # screen.blit(background,(0,0))
    for i in range(9):
        if contents[i] == "x":
            square = board[i]
            pg.draw.line(screen, "red", square.topleft, square.bottomright, 12)
            pg.draw.line(screen, "red", square.topright, square.bottomleft, 12)
        elif contents[i] == "o":
            square = board[i]
            pg.draw.circle(screen, "blue", square.center, 145, 12)

    for square in board:
        pg.draw.rect(screen, "black", square, 5)

    pg.display.flip()

    # pg.draw.rect(screen, pg.Color("blue"),(200, 300, 70, 100))


def get_board():
    # создаем поле
    board = []
    for top in range(0, 600 + 1, 300):
        for left in range(0, 600 + 1, 300):
            square = pg.Rect(left, top, WIDTH / 3, HEIGHT / 3)
            board.append(square)
    return board


def start_music():
    pg.mixer.music.load("tic tac toe/Музыка для игры на pygame.mp3")
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)


def mainloop(screen, board, contents, click_sound):
    turn = 0
    winner = None

    # основной цикл
    while True:

        draw(screen, board, contents, )

        # события
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                number_of_board = get_square_number(mouse_pos)

                # если ход x
                if turn % 2 == 0:
                    if contents[number_of_board] is None:
                        contents[number_of_board] = "x"
                        click_sound.play()
                        turn += 1

                else:
                    if contents[number_of_board] is None:
                        contents[number_of_board] = "o"
                        turn += 1
                        click_sound.play()
                if turn > 4:
                    for comb in WIN_COMBINATIONS:
                        # comb(0,4,8)
                        if contents[comb[0]] == "o" and contents[comb[1]] == "o" and contents[comb[2]] == "o":
                            winner = "o"
                            return winner

                        elif contents[comb[0]] == "x" and contents[comb[1]] == "x" and contents[comb[2]] == "x":
                            winner = "x"
                            return winner

                if turn == 9:
                    return winner


def get_square_number(mouse_pos):
    x, y = mouse_pos
    # первый столбик
    if x < 300:
        if y < 300:
            return 0
        elif y < 600:
            return 3
        else:
            return 6
    elif x < 600:
        if y < 300:
            return 1
        elif y < 600:
            return 4
        else:
            return 7
    elif x < 900:
        if y < 300:
            return 2
        elif y < 600:
            return 5
        else:
            return 8


def win_screen(winner, screen):
    pg.font.init()
    font = pg.font.SysFont("stheitimedium", 60, True, False)
    if winner == "x":
        text = font.render("Победа крестиков!", True, "green")  # создать остальные
    elif winner == "o":
        text =  font.render("Победа ноликов!", True, "green")
    else:
        text = font.render("Ничья!", True, "grey")
    screen.blit(text, (0, 400))
    pg.display.flip()
    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False


if __name__ == "__main__":
    main()
