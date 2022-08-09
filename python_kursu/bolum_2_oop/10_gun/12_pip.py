# paketleri otomatik yükler
# Terminal Menüsünden - Yeni terminal veya cmd penceresinden
# pip --version # versiyonu verir
# pip install paket_adı

# tek paket kurulmaz. her paket için gerekli başka paketler de bulunur
# bu paketlere bağımlılık denir. bu paketleri de yükler.

# pip install pygame

import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            run = False
