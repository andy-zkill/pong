# Imports
import pygame

# Pygame init
pygame.init()
pygame.mixer.init()

font = pygame.font.Font("prstart.ttf", 25)
button_font = pygame.font.Font("prstart.ttf", 12)
title_font = pygame.font.Font("prstart.ttf", 45)

block_sfx = pygame.mixer.Sound('block.ogg')
point_sfx = pygame.mixer.Sound('win.ogg')

# Screen Settings
screen_widht = 800
screen_height = 500

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_widht, screen_height))
pygame.display.set_caption("Pong")

option = 0

# Rects
ball = pygame.Rect(screen_widht / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(10, screen_height / 2 - 70, 10, 140)
player_2 = pygame.Rect(screen_widht - 20, screen_height / 2 - 70, 10, 140)
button_player_vs_player = pygame.Rect(screen_widht / 2 + 75, screen_height / 2 - 20, 200, 100)
button_player_vs_ai = pygame.Rect(screen_widht / 2 - 270, screen_height / 2 - 20, 200, 100)

# Global variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
player_2_speed = 0

player_score = 0
player_2_score = 0

while True:
    while option == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if button_player_vs_ai.left <= pos[0] <= button_player_vs_ai.right and button_player_vs_ai.top <= pos[
                    1] <= button_player_vs_ai.bottom:
                    option = 1
                    print(option)
                if button_player_vs_player.left <= pos[
                    0] <= button_player_vs_player.right and button_player_vs_player.top <= pos[
                    1] <= button_player_vs_player.bottom:
                    option = 2
                    print(option)
        game_name = title_font.render("Pong do Dedé", False, (75, 0, 130))
        player_vs_ai_text = button_font.render("Player vs Ai", False, (138, 43, 226))
        player_vs_player_text = button_font.render("Player vs Player", False, (138, 43, 226))

        screen.fill((230, 230, 250))
        pygame.draw.rect(screen, (75, 0, 130), button_player_vs_player)
        pygame.draw.rect(screen, (75, 0, 130), button_player_vs_ai)

        screen.blit(game_name, (screen_widht / 2 - 260, screen_height / 2 - 150))
        screen.blit(player_vs_ai_text, (screen_widht / 2 - 240, screen_height / 2 + 20))
        screen.blit(player_vs_player_text, (screen_widht / 2 + 80, screen_height / 2 + 20))

        clock.tick(60)
        pygame.display.flip()
        pygame.time.delay(5)
    while option == 1:
        # Ball animation
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Colisions

        # Borders
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        # Player point
        if ball.left <= 0:
            pygame.mixer.Sound.play(point_sfx)
            player_score += 1
            ball.x = screen_widht / 2 - 15
            ball.y = screen_height / 2 - 15
            player.y = screen_height / 2 - 70
            player_2.y = screen_height / 2 - 70

        # AI point
        if ball.right >= screen_widht:
            pygame.mixer.Sound.play(point_sfx)
            player_2_score += 1
            ball.x = screen_widht / 2 - 15
            ball.y = screen_height / 2 - 15
            player.y = screen_height / 2 - 70
            player_2.y = screen_height / 2 - 70

        # Player Block
        if ball.colliderect(player):
            pygame.mixer.Sound.play(block_sfx)
            if abs(player.top - ball.bottom) < 10:
                ball_speed_y *= -1
            if abs(player.bottom - ball.top) < 10:
                ball_speed_y *= -1
            if abs(player.left - ball.right) < 10:
                ball_speed_x *= -1
            if abs(player.right - ball.left) < 10:
                ball_speed_x *= -1

        # AI Block
        if ball.colliderect(player_2):
            pygame.mixer.Sound.play(block_sfx)
            if abs(player_2.top - ball.bottom) < 10:
                ball_speed_y *= -1
            if abs(player_2.bottom - ball.top) < 10:
                ball_speed_y *= -1
            if abs(player_2.left - ball.right) < 10:
                ball_speed_x *= -1
            if abs(player_2.right - ball.left) < 10:
                ball_speed_x *= -1

        # AI
        if player_2.top < ball.y:
            player_2.y += 12
        if player_2.bottom > ball.y:
            player_2.y -= 12

        # Players colision
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
        if player_2.top <= 0:
            player_2.top = 0
        if player_2.bottom >= screen_height:
            player_2.bottom = screen_height

        # Events
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            # Keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_speed += 12
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_speed -= 12
                if event.key == pygame.K_BACKSPACE:
                    option = 0
                    player_2_score = 0
                    player_score = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player_speed -= 12
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player_speed += 12
                if event.key == pygame.K_BACKSPACE:
                    option = 0
                    player_2_score = 0
                    player_score = 0
            player.y += player_speed
            player_2.y += player_2_speed

        # Drawing
        screen.fill((230, 230, 250))
        pygame.draw.ellipse(screen, (75, 0, 130), ball)
        pygame.draw.rect(screen, (75, 0, 130), player)
        pygame.draw.rect(screen, (75, 0, 130), player_2)
        pygame.draw.aaline(screen, (75, 0, 130), (screen_widht / 2, 0), (screen_widht / 2, 500), 500)

        score = font.render(f"{player_2_score}x{player_score}", False, (75, 0, 130))
        author = font.render("Pong do Dedé", False, (75, 0, 130))

        screen.blit(score, (screen_height / 2 - 35, 0))
        screen.blit(author, (screen_height / 2 - 150, 450))
        # Updating
        clock.tick(60)
        pygame.display.flip()
        pygame.time.delay(5)
    while option == 2:
        # Ball animation
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Colisions

        # Borders
        if ball.top <= 0 or ball.bottom >= screen_height:
            ball_speed_y *= -1

        # Player 1 point
        if ball.left <= 0:
            pygame.mixer.Sound.play(point_sfx)
            player_score += 1
            ball.x = screen_widht / 2 - 15
            ball.y = screen_height / 2 - 15
            player.y = screen_height / 2 - 70
            player_2.y = screen_height / 2 - 70

        # Player 2 point
        if ball.right >= screen_widht:
            pygame.mixer.Sound.play(point_sfx)
            player_2_score += 1
            ball.x = screen_widht / 2 - 15
            ball.y = screen_height / 2 - 15
            player.y = screen_height / 2 - 70
            player_2.y = screen_height / 2 - 70

        # Player 1 Block
        if ball.colliderect(player):
            pygame.mixer.Sound.play(block_sfx)
            if abs(player.top - ball.bottom) < 10:
                ball_speed_y *= -1
            if abs(player.bottom - ball.top) < 10:
                ball_speed_y *= -1
            if abs(player.left - ball.right) < 10:
                ball_speed_x *= -1
            if abs(player.right - ball.left) < 10:
                ball_speed_x *= -1

        # Player 2 Block
        if ball.colliderect(player_2):
            pygame.mixer.Sound.play(block_sfx)
            if abs(player_2.top - ball.bottom) < 10:
                ball_speed_y *= -1
            if abs(player_2.bottom - ball.top) < 10:
                ball_speed_y *= -1
            if abs(player_2.left - ball.right) < 10:
                ball_speed_x *= -1
            if abs(player_2.right - ball.left) < 10:
                ball_speed_x *= -1

        # Players colision
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height
        if player_2.top <= 0:
            player_2.top = 0
        if player_2.bottom >= screen_height:
            player_2.bottom = screen_height

        # Events
        for event in pygame.event.get():
            # Quit
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            # Keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player_speed += 12
                if event.key == pygame.K_w:
                    player_speed -= 12
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    player_speed -= 12
                if event.key == pygame.K_w:
                    player_speed += 12

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_k:
                    player_2_speed += 12
                if event.key == pygame.K_i:
                    player_2_speed -= 12
                if event.key == pygame.K_BACKSPACE:
                    option = 0
                    player_2_score = 0
                    player_score = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_k:
                    player_2_speed -= 12
                if event.key == pygame.K_i:
                    player_2_speed += 12
                if event.key == pygame.K_BACKSPACE:
                    option = 0
                    player_2_score = 0
                    player_score = 0
            player.y += player_speed
            player_2.y += player_2_speed

        # Drawing
        screen.fill((230, 230, 250))
        pygame.draw.ellipse(screen, (75, 0, 130), ball)
        pygame.draw.rect(screen, (75, 0, 130), player)
        pygame.draw.rect(screen, (75, 0, 130), player_2)
        pygame.draw.aaline(screen, (75, 0, 130), (screen_widht / 2, 0), (screen_widht / 2, 500), 500)

        score = font.render(f"{player_2_score}x{player_score}", False, (75, 0, 130))
        author = font.render("Pong do Dedé", False, (75, 0, 130))

        screen.blit(score, (screen_height / 2 - 35, 0))
        screen.blit(author, (screen_height / 2 - 150, 450))

        # Updating
        clock.tick(60)
        pygame.display.flip()
        pygame.time.delay(5)
