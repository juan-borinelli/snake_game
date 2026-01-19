import curses
import time
import random
def draw_screen(window):
    window.clear()
    window.border(0)#borda no terminal

def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)

def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char = 'C')
    body = snake[1:]
    for body_part in body:
        draw_actor(actor=body_part, window=window, char = '0')

def get_new_direction(window, timeout):
        window.timeout(timeout) #seletor de dificuldade
        direction = window.getch()
        if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_DOWN]:
            return direction
        else:
            None

def move_snake(snake, direction):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    snake.pop()

def move_actor(actor, direction):
    match direction:
            case curses.KEY_UP:
                actor[0] -= 1
            case curses.KEY_LEFT:
                actor[1] -= 1
            case curses.KEY_RIGHT:
                actor[1] += 1
            case curses.KEY_DOWN:
                actor[0] += 1
    
def actor_hit_border(actor, window):
    height, width = window.getmaxyx()
    if actor[0] <= 0 or actor[0] >= height-1:
        return True
    if actor[1] <= 0 or actor[1] >= width-1:
        return True
    return False

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(actor=head, window=window)

def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2), random.randint(1, width-2)]

def snake_hit_fruit(snake, fruit):
    head=snake[0]
    return fruit in snake

def grow_snake(snake):
    tam_snake=len(snake)
    add = snake[tam_snake-1].copy()
    snake.append(add)

def snake_hit_itself(snake):
    head = snake[0]
    return head in snake[1:]

def direction_is_opposite(direction, current_direction):
     match direction:
            case curses.KEY_UP:
                return current_direction == curses.KEY_DOWN
            case curses.KEY_LEFT:
                return current_direction == curses.KEY_RIGHT
            case curses.KEY_RIGHT:
                return current_direction == curses.KEY_LEFT
            case curses.KEY_DOWN:
                return current_direction == curses.KEY_UP

def finish_game(score, window):
    height, width = window.getmaxyx()
    msg = f'Voce perdeu! Sua pontuação é: {score} frutas comidas.'
    y = int(height/2)
    x = int((width -len(msg))/2)
    window.addstr(y, x, msg)
    window.refresh()
    time.sleep(2)

def game_loop(window, game_speed):
    #setup inicial
    curses.curs_set(0) #eliminar cursor
    snake = [ 
            [10,15],
            [9,15],
            [8,15],
            [7,15]
            ]
    current_direction = curses.KEY_DOWN
    fruit = get_new_fruit(window=window)
    score = 0

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char= curses.ACS_DIAMOND)
        direction = get_new_direction(window=window, timeout=game_speed)

        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction
        move_snake(snake=snake, direction=current_direction)
        if snake_hit_border(snake=snake, window=window):
            break
        current_direction = direction
        if snake_hit_itself(snake=snake):
            break
        if snake_hit_fruit(snake=snake, fruit=fruit):
            score += 1
            fruit = get_new_fruit(window=window)
            grow_snake(snake=snake)
    finish_game(score=score, window=window)

def select_difficulty():
    difficulty = {
    '1' : 1000,
    '2' : 500,
    '3' : 250,
    '4' : 125,
    '5' : 67,
    }
    while True:
        answer = input('Selecione a dificuldade de 1 a 5: ')
        game_speed = difficulty.get(answer)
        if game_speed is not None:
            return game_speed
        print('Escolha uma dificuldade de 1 a 5!')



if __name__ == '__main__':
    curses.wrapper(game_loop, game_speed=select_difficulty())
