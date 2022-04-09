"""Demo of pygame."""

# Import and initialize the pygame library
import pygame
 
pygame.init()
 
# Set up the drawing window
screen = pygame.display.set_mode([800, 500])
                               
# pygame clock object controls tick rate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True

# Creates Rectangle object at x = 20, y = 20, width = 50, height = 50
rect: pygame.Rect = pygame.Rect(20, 20, 50, 50)
coins: list[pygame.Rect] = [pygame.Rect(200, 300, 25, 25), pygame.Rect(400, 400, 25, 25), pygame.Rect(600, 200, 25, 25)]
 
while running:
    clock.tick(60)
 
    # Fill background
    screen.fill((120, 200, 255))

    # get_pos() gets the (x,y) position of the mouse and that is then offset by 25
    rect.x = pygame.mouse.get_pos()[0] - 25
    rect.y = pygame.mouse.get_pos()[1] - 25

    # Draw the rectangle
    pygame.draw.rect(screen, (150, 10, 245), rect)

    # draws the circles for coins (window, color(rgb), position (x,y), radius)
    # for i in range(0, len(coins)):
    #     pygame.draw.circle(screen, (235, 162, 52), (coins[i].centerx, coins[i].centery), 15)

    # Rect collision and draw circles
    for coin in coins:
        pygame.draw.circle(screen, (235, 162, 52), (coin.centerx, coin.centery), 15)
        hit = coin.colliderect(rect)
        if hit:
            coins.remove(coin)

    # Checks every frame for any user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                coins.append(pygame.Rect(500, 400, 25, 25))
   
    pygame.display.flip()
 
# Done! Time to quit.
pygame.quit()