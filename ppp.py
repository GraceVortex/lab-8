import pygame
import math

def main():
    # initialize pygame
    pygame.init()
    # set up the screen
    screen = pygame.display.set_mode((640, 480))
    # set up the clock for controlling the frame rate
    clock = pygame.time.Clock()
    
    # set the initial radius for drawing lines
    radius = 15
    # set the initial drawing color
    mode = 'blue'
    # list to store points for drawing lines
    points = []
    # variable to store the current drawing shape
    draw_shape = 'line'
    # variable to store the starting position for drawing shapes
    start_pos = None  
    
    while True:
        # fill the screen with black
        screen.fill((0, 0, 0))
        
        # check for events
        for event in pygame.event.get():
            # if the window is closed, exit the program
            if event.type == pygame.QUIT:
                return
            # if the left mouse button is pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # if drawing a line, increase the radius
                    if draw_shape == 'line':
                        radius = min(200, radius + 1)
                    # if drawing a circle or rectangle, set the starting position
                    elif draw_shape in ['circle', 'rectangle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        start_pos = event.pos
                # if the right mouse button is pressed
                elif event.button == 3:
                    # if drawing a line, decrease the radius
                    if draw_shape == 'line':
                        radius = max(1, radius - 1)
            # if the mouse is moved while the left mouse button is pressed
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  
                    # if drawing a line, add points to the list
                    if draw_shape == 'line':
                        points.append(event.pos)
                        points = points[-256:]
                    # if drawing a circle or rectangle, update the end position
                    elif draw_shape in ['circle', 'rectangle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        end_pos = event.pos
            # if a key is pressed
            elif event.type == pygame.KEYDOWN:
                # switch drawing modes based on key pressed
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
                    mode = (0, 0, 0)  # set color to black (eraser mode)
                elif event.key == pygame.K_q:
                    draw_shape = 'square'
                elif event.key == pygame.K_t:
                    draw_shape = 'right_triangle'
                elif event.key == pygame.K_u:
                    draw_shape = 'equilateral_triangle'
                elif event.key == pygame.K_d:
                    draw_shape = 'rhombus'
        
        # draw shapes
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
        elif draw_shape == 'square':
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
                pygame.draw.rect(screen, mode, rect)
        elif draw_shape == 'right_triangle':
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                pygame.draw.polygon(screen, mode, [start_pos, (end_pos[0], start_pos[1]), end_pos])
        elif draw_shape == 'equilateral_triangle':
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                side = math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)
                height = (math.sqrt(3) / 2) * side
                pygame.draw.polygon(screen, mode, [start_pos, (end_pos[0], start_pos[1]), ((start_pos[0] + end_pos[0]) / 2, start_pos[1] - height)])
        elif draw_shape == 'rhombus':
            if start_pos:
                end_pos = pygame.mouse.get_pos()
                width = abs(end_pos[0] - start_pos[0])
                height = abs(end_pos[1] - start_pos[1])
                pygame.draw.polygon(screen, mode, [(start_pos[0] + width / 2, start_pos[1]), (end_pos[0], start_pos[1] + height / 2), (start_pos[0] + width / 2, end_pos[1]), (start_pos[0], start_pos[1] + height / 2)])
        
        # update the display
        pygame.display.flip()
        # control the frame rate
        clock.tick(60)

main()
