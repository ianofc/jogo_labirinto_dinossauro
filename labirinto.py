import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do Labirinto")

# Cores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Fonte para mensagens
font = pygame.font.Font(None, 36)

# Carrega a imagem do dinossauro
try:
    dino_image = pygame.image.load("dinossauro.png")
except pygame.error as e:
    print(f"Erro ao carregar a imagem: {e}")
    pygame.quit()
    exit()

# Redimensiona a imagem do dinossauro para caber nas células
cell_size = 40
dino_image = pygame.transform.scale(dino_image, (cell_size, cell_size))
dino_rect = dino_image.get_rect()
dino_rect.topleft = (0, 0)

# Configurações do labirinto
maze_width = screen_width // cell_size
maze_height = screen_height // cell_size

# Função para gerar o labirinto com caminho garantido
def generate_maze_with_path(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    path = [(0, 0)]  # Caminho começa no ponto (0, 0)
    x, y = 0, 0

    directions = [(0, 1), (1, 0)]  # Apenas para baixo e para direita, garantindo caminho direto
    while (x, y) != (width - 1, height - 1):  # Até chegar ao canto inferior direito
        dx, dy = random.choice(directions)
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            path.append((nx, ny))
            maze[y][x] = 0
            x, y = nx, ny

    maze[height - 1][width - 1] = 0  # Marca o destino como acessível

    # Cria paredes aleatórias sem bloquear o caminho gerado
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1 and random.random() < 0.7:  # 70% de chance de ser parede
                maze[y][x] = 1
            else:
                maze[y][x] = 0

    for x, y in path:
        maze[y][x] = 0  # Garante que o caminho gerado está livre

    return maze

# Gera o labirinto
maze = generate_maze_with_path(maze_width, maze_height)

# Função para desenhar o labirinto
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if (x, y) == (0, 0):  # Ponto A
                color = GREEN
            elif (x, y) == (len(maze[0]) - 1, len(maze) - 1):  # Ponto B
                color = RED
            else:
                color = YELLOW if cell == 0 else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

# Verifica colisão com paredes
def check_collision(maze, rect):
    corners = [
        (rect.left, rect.top),  # Canto superior esquerdo
        (rect.right - 1, rect.top),  # Canto superior direito
        (rect.left, rect.bottom - 1),  # Canto inferior esquerdo
        (rect.right - 1, rect.bottom - 1),  # Canto inferior direito
    ]
    for x, y in corners:
        maze_x = x // cell_size
        maze_y = y // cell_size
        if 0 <= maze_x < len(maze[0]) and 0 <= maze_y < len(maze):
            if maze[maze_y][maze_x] == 1:
                return True
    return False

# Exibe a mensagem de vitória
def show_message(message, options):
    screen.fill(BLACK)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(text, text_rect)

    # Exibe as opções
    option_texts = []
    for i, option in enumerate(options):
        opt_text = font.render(option, True, WHITE)
        opt_rect = opt_text.get_rect(center=(screen_width // 2, screen_height // 2 + i * 50))
        screen.blit(opt_text, opt_rect)
        option_texts.append((opt_text, opt_rect))

    pygame.display.flip()
    return option_texts

# Função principal do jogo
def main():
    global dino_rect, maze
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and dino_rect.left > 0:
            dino_rect.move_ip(-5, 0)
            if check_collision(maze, dino_rect):
                dino_rect.move_ip(5, 0)
        if keys[pygame.K_RIGHT] and dino_rect.right < screen_width:
            dino_rect.move_ip(5, 0)
            if check_collision(maze, dino_rect):
                dino_rect.move_ip(-5, 0)
        if keys[pygame.K_UP] and dino_rect.top > 0:
            dino_rect.move_ip(0, -5)
            if check_collision(maze, dino_rect):
                dino_rect.move_ip(0, 5)
        if keys[pygame.K_DOWN] and dino_rect.bottom < screen_height:
            dino_rect.move_ip(0, 5)
            if check_collision(maze, dino_rect):
                dino_rect.move_ip(0, -5)

        # Verifica se o dinossauro chegou ao ponto final
        if dino_rect.colliderect(
            pygame.Rect((maze_width - 1) * cell_size, (maze_height - 1) * cell_size, cell_size, cell_size)
        ):
            options = show_message("Você venceu! Deseja começar de novo ou sair?", ["[1] Começar de novo", "[2] Sair"])
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        waiting = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:  # Reiniciar
                            maze = generate_maze_with_path(maze_width, maze_height)
                            dino_rect.topleft = (0, 0)
                            waiting = False
                        elif event.key == pygame.K_2:  # Sair
                            running = False
                            waiting = False

        screen.fill(BLACK)
        draw_maze(maze)
        screen.blit(dino_image, dino_rect)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
