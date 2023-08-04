import pygame
import pygame_gui


pygame.init()

pygame.display.set_caption('Game')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

font = pygame.font.SysFont('arial', 32)

follow = font.render("Меню",0, (255, 255, 255))

manager = pygame_gui.UIManager((800, 600))

new_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 150), (700, 100)),
                                            text='Новая игра',
                                            manager=manager)

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 250), (700, 100)),
                                            text='Продолжить игру',
                                            manager=manager)

donate_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 350), (700, 100)),
                                            text='Поддержать',
                                            manager=manager)

quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 450), (700, 100)),
                                            text='Выйти',
                                            manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == new_button:
             if event.ui_element == start_button:
              if event.ui_element == donate_button:
               if event.ui_element == quit_button:
                  is_running = False
        manager.process_events(event)
    background.blit(follow, (350, 50))
    pygame.display.update()

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
