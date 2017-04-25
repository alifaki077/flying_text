from sys import argv
from time import sleep
from shutil import get_terminal_size


def show(screen, sizex, sizey):
    print('\033[H')  # move to the top
    print('\033[J')  # clear the screen
    for i in range(sizex + 1):
        for j in range(sizey + 1):
            print(screen[(i, j)] if (i, j) in screen else " ", end="")
        print()


def move(k, x_speed, y_speed):
    return (k[0] + x_speed, k[1] + y_speed)


def check_collide(k, sizex, sizey):
    if k[0] < 0:
        return "T"
    elif k[0] > sizex:
        return "B"
    elif k[1] < 0:
        return "L"
    elif k[1] > sizey:
        return "R"


def next_move(screen, x_speed, y_speed, sizex, sizey):
    new_screen = {}
    collide = set()
    for k, v in screen.items():
        k2 = move(k, x_speed, y_speed)
        tmp_k = move(k2, x_speed, y_speed)
        collide.add(check_collide(tmp_k, sizex, sizey))
        new_screen[k2] = v

    if "T" in collide or "B" in collide:
        x_speed *= -1
    if "R" in collide or "L" in collide:
        y_speed *= -1
    return new_screen, x_speed, y_speed


if __name__ == "__main__":
    try:
        text = argv[1]
    except IndexError:
        text="i can fly"
    screen = {(0, i):text[i] for i in range(len(text))}
    x_speed = y_speed = 1
    while True:
        sizey, sizex = get_terminal_size((50, 50))
        sizey -= 1
        sizex -= 2
        show(screen, sizex, sizey)
        screen, x_speed, y_speed = next_move(screen, x_speed, y_speed, sizex, sizey)
        sleep(0.1)