import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    draw_shape = 'line'
    start_pos = None  # Variable to store the starting position for drawing shapes
    
    while True:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if draw_shape == 'line':
                        radius = min(200, radius + 1)
                    elif draw_shape == 'circle':
                        start_pos = event.pos
                    elif draw_shape == 'rectangle':
                        start_pos = event.pos
                elif event.button == 3:
                    if draw_shape == 'line':
                        radius = max(1, radius - 1)
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button is held down
                    if draw_shape == 'line':
                        points.append(event.pos)
                        points = points[-256:]
                    elif draw_shape == 'circle':
                        end_pos = event.pos
                        radius = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    elif draw_shape == 'rectangle':
                        end_pos = event.pos
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    draw_shape = 'circle'
                elif event.key == pygame.K_s:
                    draw_shape = 'rectangle'
                elif event.key == pygame.K_l:
                    draw_shape = 'line'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_e:
                    mode = (0, 0, 0)  # Set color to black (eraser mode)
        
        # Draw shapes
        if draw_shape == 'line':
            for i in range(len(points) - 1):
                pygame.draw.line(screen, mode, points[i], points[i + 1], radius * 2)
        elif draw_shape == 'circle':
            if start_pos:
                pygame.draw.circle(screen, mode, start_pos, radius, 2)
        elif draw_shape == 'rectangle':
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                rect = pygame.Rect(start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                pygame.draw.rect(screen, mode, rect)
        
        pygame.display.flip()
        clock.tick(60)

main()
