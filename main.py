import pygame
import random
import time

pygame.init()
width, height = 3070, 1590
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AimLabJr")

# Colors
backgroundColor = (44, 42, 44)
targetColor = (0, 207, 255)
textColor = (0, 0, 0)
targetRadius = 50

font = pygame.font.Font("freesansbold.ttf", 80)  

def draw_target(surface, x, y, alpha):
    pygame.draw.circle(surface, targetColor + (alpha,), (x, y), targetRadius)

def main():
    score = 0
    clock = pygame.time.Clock()
    target_x, target_y = random.randint(targetRadius, width - targetRadius), random.randint(targetRadius, height - targetRadius) 
    t_end = time.time() + 60
    while time.time() < t_end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = (target_x - mouse_x)**2 + (target_y - mouse_y)**2
                if distance < targetRadius**2:
                    score += 1
                    target_x, target_y = random.randint(targetRadius, width - targetRadius), random.randint(targetRadius, height - targetRadius) 
        screen.fill(backgroundColor)

        draw_target(screen, target_x, target_y - 10, 255)
        score_text = font.render(f"{score}", True, textColor)
        screen.blit(score_text, (100, 10))
        t = font.render(f"{int(t_end - time.time())}", True, textColor)
        screen.blit(t, (width - 100,10))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()