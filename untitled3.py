import turtle
import random

w = 500
h = 500
food_size = 10
delay = 100

offsets = {
    "up": (0, 10),
    "down": (0, -10),
    "left": (-10, 0),
    "right": (10, 0)
}

def reset():
    global snake, snake_dir, food_position, pen\
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    move_snake()
    
def move_snake():
    global snake_dir
    
    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
   
    
    if new_head in snake[:-1]:
        reset()
    else:
        snake.append(new_head)
        
        
        if not food_collison():
            snake.pop(0)
            
            
        if snake[-1][0] > w / 2:
            snale[-1][0] -= w
        elif snake[-1][0] < - w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2:
            snake[-1][1] -= h
        elif snake[-1][1] < -h /2:
            snake[-1][1] += h
            
            
            pen.clearstanps()