import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            # dá funcionalidade para as opções do menu
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]: # três modos de jogo
                player_score = [0, 0]  # [Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score) # passa o modo de jogo e os scores dos jogadores
            elif menu_return == MENU_OPTION[3]:
                score.show() # carrega a tela de score
            elif menu_return == MENU_OPTION[4]: # fechar jogo
                pygame.quit() # close window
                quit() # end game
            else:
                pass
