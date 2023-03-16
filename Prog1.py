import pygame

pygame.init()

# Definir as dimensões da tela
screen_width = 1366
screen_height = 768

# Configurar a tela em modo de tela cheia
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Definir o título da janela
pygame.display.set_caption("CRM - SST - Basttos Engenharia")

# Definir a cor de fundo da tela
background_color = (135, 206, 250)

# Definir a cor das fontes
blue_color = (0, 0, 128)
red_color = (255, 0, 0)

# Criar um objeto de fonte
title_font = pygame.font.SysFont('arial', 30)
subtitle_font = pygame.font.SysFont('arial', 16)

# Criar uma superfície de texto com o título
title_surface = title_font.render('CRM - SST - BASTTOS TECNOLOGIA', True, blue_color)

# Criar uma superfície de texto com a mensagem de pressionar qualquer tecla
subtitle_surface = subtitle_font.render('Pressione qualquer tecla para continuar.', True, red_color)

# Obter o retângulo do título
title_rect = title_surface.get_rect()

# Obter o retângulo da mensagem de pressionar qualquer tecla
subtitle_rect = subtitle_surface.get_rect()

# Centralizar o retângulo do título na tela
title_rect.center = (screen_width // 2, screen_height // 2)

# Definir a posição da mensagem de pressionar qualquer tecla abaixo do título
subtitle_rect.midtop = (screen_width // 2, title_rect.bottom + 20)

# Preencher a tela com a cor de fundo
screen.fill(background_color)

# Blit o título e a mensagem de pressionar qualquer tecla na tela
screen.blit(title_surface, title_rect)
screen.blit(subtitle_surface, subtitle_rect)

# Atualizar a tela
pygame.display.flip()

# Aguardar até que uma tecla seja pressionada para fechar a janela
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()
