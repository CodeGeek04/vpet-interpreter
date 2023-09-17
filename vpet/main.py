import pygame
import subprocess
import os

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Program')

button_width = 200
button_height = 50
button_color = (255, 0, 0)
button_text = 'Run Speech Recognition'
button_font = pygame.font.Font(None, 30)
button_text_render = button_font.render(button_text, True, (255, 255, 255))
button_rect = pygame.Rect((window_width - button_width) // 2, (window_height - button_height) // 2, button_width, button_height)

def run_command_in_new_terminal(command):
    subprocess.Popen(['start', 'cmd', '/c', 'start /min cmd /k ' + command], shell=True)

def run_speech_recognition():
    # os.system('python speech_recog.py')
    # pygame.display.iconify()
    # os.chdir('Sources/Windows')
    # os.system('python main.py')
    pygame.display.iconify()
    run_command_in_new_terminal('python speech_recog.py')
    os.chdir('Sources/Windows')
    run_command_in_new_terminal('python main.py')




running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                run_speech_recognition()

    window.fill((255, 255, 255))
    pygame.draw.rect(window, button_color, button_rect)
    window.blit(button_text_render, (button_rect.x + (button_width - button_text_render.get_width()) // 2, button_rect.y + (button_height - button_text_render.get_height()) // 2))
    pygame.display.flip()
