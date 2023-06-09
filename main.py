import pygame
from data import *
from pong import *
pygame.init()

window = pygame.display.set_mode((setting_win['WIDTH'], setting_win["HEIGHT"] ))
pygame.display.set_caption("PingPong")

def run():
    game = True
    
    
    clock = pygame.time.Clock()
    board_left = Board(     15,
                            setting_win['HEIGHT'] // 2 - setting_board['HEIGHT'] // 2,
                            setting_board['WIDTH'],
                            setting_board['HEIGHT'])
    board_right = Board(    setting_win['WIDTH'] - setting_board['WIDTH'] - 15,
                            setting_win['HEIGHT'] // 2 - setting_board['HEIGHT'] // 2,
                            setting_board['WIDTH'],
                            setting_board['HEIGHT'])
    ball = Ball(    setting_win["WIDTH"] // 2 - setting_ball["RADIUS"],
                    setting_win['HEIGHT'] // 2 - setting_ball["RADIUS"],
                    setting_ball['RADIUS']
    )
    menu = Menu(200, 50, 4)
    
    while game:
        events = pygame.event.get()
        if ball.which_window==1:
            window.fill ((0,0,0))
            pygame.draw.rect(window, (255,255,255), board_right)
            pygame.draw.rect(window, (255,255,255), board_left)
            pygame.draw.circle(window, (255,255,255), (ball.X, ball.Y), ball.RADIUS)
            board_left.move()
            board_right.move()
            ball.move(board_left, board_right, window)

            for event in events :
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        board_left.MOVE["UP"] = True
                    if event.key == pygame.K_s:
                        board_left.MOVE["DOWN"] = True
                    if event.key == pygame.K_a:
                        board_right.MOVE["UP"] = True
                    if event.key == pygame.K_d:
                        board_right.MOVE["DOWN"] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        board_left.MOVE["UP"] = False
                    if event.key == pygame.K_s:
                        board_left.MOVE["DOWN"] = False
                    if event.key == pygame.K_a:
                        board_right.MOVE["UP"] = False
                    if event.key == pygame.K_d:
                        board_right.MOVE["DOWN"] = False





            clock.tick(90)
        elif ball.which_window == 0:
            
            menu.draw_menu(window)
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    ball.which_window = menu.click(event.pos)
                    if ball.which_window==1:
                        ball.restart(board_left, board_right, window)
                    elif ball.which_window==4:
                        game=False

        elif ball.which_window == 3:
            menu.show_history(window)
            for event in events:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        ball.which_window=0


        for event in events:
            if event.type == pygame.QUIT:
                game = False
        print(ball.which_window)
        pygame.display.flip()



run()