import pygame, sys
from pygame.locals import *
pygame.init()

#Set the screen.
Screen = pygame.display.set_mode((800, 800))

#Set the name of the game.
pygame.display.set_caption("Quoridor - Ultimate Edition")

#Set the icon of the game.
pygame.display.set_icon( pygame.image.load("app.png") )

#Incidential music.
pygame.mixer.music.load("Susmaz.wav")
pygame.mixer.music.play(-1)

#Primitive locations for the players.
Location1 = [300, 0]
Location2 = [400, 700]

#Each player has five walls.
Number_of_walls1 = 10
Number_of_walls2 = 10

#Main loop for starting the game.
while True:
    #Background.
    Screen.blit(pygame.transform.scale(pygame.image.load("Snow.jpg"), (800, 800)), (0, 0))
    
    #Welcoming text.
    pygame.font.Font(None, 25).render("Welcome, players!", True, (255, 255, 255)).get_rect().center = (400, 300)
    Screen.blit(pygame.font.Font(None, 25).render("Welcome, players!", True, (255, 255, 255)), pygame.font.Font(None, 25).render("Welcome, players!", True, (0, 0, 0)).get_rect())

    #Player one's turn.
    for event in pygame.event.get():
        #Exit keys.
        if event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE ):
            pygame.quit()
            sys.exit()

        #Moving and placing walls keys.
        if event.type == KEYDOWN:
            #Moving right.
            if event.key == K_RIGHT:
                if Location1[0] + 100 == Location2[0] and Location1[1] == Location2[1]:
                    Location1[0] += 200
                    break
                else:
                    Location1[0] += 100
                    break

            #Moving left.
            elif event.key == K_LEFT:
                if Location1[0] - 100 == Location2[0] and Location1[1] == Location2[1]:
                    Location1[0] -= 200
                    break
                else:
                    Location1[0] -= 100
                    break
            #Moving down.
            elif event.key == K_DOWN:
                if Location1[0] == Location2[0] and Location1[1] + 100 == Location2[1]:
                    Location1[1] += 200
                    break
                else:
                    Location1[1] += 100
                    break

            #Moving up.
            elif event.key == K_UP:
                if Location1[0] == Location2[0] and Location1[1] - 100 == Location2[1]:
                    Location1[1] -= 200
                    break
                else:
                    Location1[1] -= 100
                    break
                    
            #Placing Horizontal wall.
            elif event.key == K_h:
                pygame.draw.line(Screen, (100, 40, 0), (Location2[0], Location2[1] - 13), (Location2[0] + 100, Location2[1] - 13), 20)
                Number_of_walls1 -= 1
                break
                
            #Placing left-handed vertical wall.
            elif event.key == K_l:
                pygame.draw.line(Screen, (100, 40, 0), (Location2[0], Location2[1]), (Location2[0], Location2[1] + 100 ), 20)
                Number_of_walls1 -= 1
                break
                    
            #Placing Right-handed vertical wall.
            elif event.key == K_r:
                pygame.draw.line(Screen, (100, 40, 0), (Location2[0] + 100, Location2[1]), (Location2[0] + 100, Location2[1] + 100 ), 20)
                Number_of_walls1 -= 1
                break
    
    #Winning conditions for player 1.
    if Location1[1] == 700:
        Screen.fill((255, 255, 255))
        pygame.font.Font(None, 25).render("PLAYER-1, WINS!", True, (0, 0, 0)).get_rect().center = (400, 300)
        Screen.blit(pygame.font.Font(None, 25).render("PLAYER-1, WINS!", True, (0, 0, 0)), pygame.font.Font(None, 25).render("PLAYER-1, WINS!", True, (0, 0, 0)).get_rect())
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                #Exit keys.
                if event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE ):
                    pygame.quit()
                    sys.exit()

    #Player two's turn.
    for event in pygame.event.get():
        #Exit keys.
        if event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE ):
            pygame.quit()
            sys.exit()

        #Moving and placing walls keys.
        if event.type == KEYDOWN:
            #Moving right.
            if event.key == K_RIGHT:
                if Location2[0] + 100 == Location1[0] and Location2[1] == Location1[1]:
                    Location2[0] += 200
                    break
                else:
                    Location2[0] += 100
                    break

            #Moving left.
            elif event.key == K_LEFT:
                if Location2[0] - 100 == Location1[0] and Location2[1] == Location1[1]:
                    Location2[0] -= 200
                    break
                else:
                    Location2[0] -= 100
                    break
                    
            #Moving down.
            elif event.key == K_DOWN:
                if Location2[0] == Location1[0] and Location2[1] + 100 == Location1[1]:
                    Location2[0] += 200
                    break
                else:
                    Location2[1] += 100
                    break

            #Moving up.
            elif event.key == K_UP:
                if Location2[0] == Location1[0] and Location2[1] - 100 == Location1[1]:
                    Location2[1] -= 200
                    break
                else:
                    Location2[1] -= 100
                    break
            
            elif event.key == K_h:
                pygame.draw.line(Screen, (100, 40, 0), (Location1[0], Location1[1] + 100), (Location1[0] + 100, Location1[1] + 100), 20)
                Number_of_walls2 -= 1
                break

            elif event.key == K_l:
                pygame.draw.line(Screen, (100, 40, 0), (Location1[0], Location1[1]), (Location1[0], Location1[1] + 100 ), 20)
                Number_of_walls2 -= 1
                break
            
            elif event.key == K_r:
                pygame.draw.line(Screen, (100, 40, 0), (Location1[0] + 100, Location1[1]), (Location1[0] + 100, Location1[1] + 100 ), 20)
                Number_of_walls2 -= 1
                break

    Screen.blit(pygame.transform.scale(pygame.image.load("One.png"), (100, 100)), (Location1[0], Location1[1]))
    Screen.blit(pygame.transform.scale(pygame.image.load("Two.png"), (100, 100)), (Location2[0], Location2[1]))
    pygame.display.update()
        
    #Winning conditions for player 2.
    if Location2[1] == 0:
        Screen.fill((255, 255, 255))
        pygame.font.Font(None, 25).render("PLAYER-2, WINS!", True, (0, 0, 0)).get_rect().center = (400, 300)
        Screen.blit(pygame.font.Font(None, 25).render("PLAYER-2, WINS!", True, (0, 0, 0)), pygame.font.Font(None, 25).render("PLAYER-2, WINS!", True, (0, 0, 0)).get_rect())
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                #Exit keys.
                if event.type == QUIT or ( event.type == KEYDOWN and event.key == K_ESCAPE ):
                    pygame.quit()
                    sys.exit()
            
#THE END
