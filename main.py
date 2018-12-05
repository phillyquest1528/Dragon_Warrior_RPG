# Things to improve:
# 1. Make sure NPCs can't walk through blocked tiles.  Limit walking distance to 1 tile.
# 2. Loading NPC for different maps
# 3. Make a map class that combines map_engine and Tiles classes
# 4. Write a print class that will show a text box like NPC dialog


import pygame, sys, time, math
from scripts.UltraColor import *
from scripts.textures import *
from scripts.globals import *
from scripts.map_engine import *
from scripts.NPC import *
from scripts.player import *
from scripts.meloonatic_gui import *

pygame.init()

FPS = 0

terrain_ME = Map_Engine()
town_ME = Map_Engine()
terrain_TS = Tiles()
town_TS = Tiles()
terrain = terrain_ME.load_map("maps\\phils_world05.map", terrain_TS)
town = town_ME.load_map("maps\\first_town02.map", town_TS)


fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\sky.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0,0))
del sky

logo_img_temp = pygame.image.load("graphics\\logo.png")
#pygame.transform.scale(logo_img_temp)
logo_img = pygame.Surface(logo_img_temp.get_size(), pygame.HWSURFACE)
logo_img.blit(logo_img_temp, (0, 0))
del logo_img_temp

dialog_background = pygame.image.load("graphics\\GUI\\dialog.png")
Dialog_Background = pygame.Surface(dialog_background.get_size(), pygame.HWSURFACE|pygame.SRCALPHA)
Dialog_Background.blit(dialog_background, (0, 0))
Dialog_Background_Width, Dialog_Background_Height = Dialog_Background.get_size()
del dialog_background



clock = pygame.time.Clock()


def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.Goldenrod)
    window.blit(fps_overlay, (0,0))

def create_window():
    # Create the window, surfaces will be drawn to here
    global window, window_height, window_width, window_title
    window_width, window_height = 800, 600
    window_title = "YouTube RPG"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

# use pygames fps counter
def count_fps():
    global FPS, deltatime

    FPS = clock.get_fps()
    if FPS > 0:
        Globals.deltatime = 1 / FPS



create_window()

player = Player("ME")
player_w, player_h = player.width, player.height
player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / terrain_TS.Size
player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / terrain_TS.Size



# Assign dialog to specific NPC
TestDialog = Dialog(text = [("hello friend", "how are you"), ("This is the next page", "cool"), ("Yawn...", "this is another mofo page")])
Globals.active_dialog = TestDialog



# Not put in a grid position
man1 = Male1("Phil",(600, 300), "world", terrain_TS.Blocked,
             dialog = Dialog(text = [("Yo bitch.", "Don't go south.  It's super crazy down there."),
                                     ("Err...", "I'm sketchy, though", "Take your chances"),
                                     ("Nah bro, I'm just fucking with you.","It's chill down there...")]))

man2 = Male1("Killer", (1200, 600), "world", terrain_TS.Blocked,
             dialog = Dialog(text = [("Killer's my name.", "13 years old."),
                                     ("Nothings's going to stop me from getting to","woodland cave.  I hear there's a powerful", "bow hidden there.")]))

man3 = Male1("Filthy Savage", (600, 400), "world", terrain_TS.Blocked,
             dialog = Dialog(text = [("ugghhh", "ugh", "ughhhhhh...."),
                                     ("*squeak", "*fart"), ("Huh...", "who's asking...I dunno")]))



man4 = Male1("Tom",(5 * Globals.tile_size, 5 * Globals.tile_size), "town", town_TS.Blocked,
             dialog = Dialog(text = [("Yo bitch.", "Don't go south.  It's super crazy down there."),
                                     ("Err...", "I'm sketchy, though", "Take your chances"),
                                     ("Nah bro, I'm just fucking with you.","It's chill down there...")]))

man5 = Male1("Dick", (7 * Globals.tile_size, 8 * Globals.tile_size), "town", town_TS.Blocked,
             dialog = Dialog(text = [("Killer's my name.", "13 years old."),
                                     ("Nothings's going to stop me from getting to","woodland cave.  I hear there's a powerful", "bow hidden there.")]))

man6 = Male1("Harry", (12 * Globals.tile_size, 15 * Globals.tile_size), "town", town_TS.Blocked,
             dialog = Dialog(text = [("ugghhh", "ugh", "ughhhhhh...."),
                                     ("*squeak", "*fart"), ("Huh...", "who's asking...I dunno")]))







# INITIALIZE GUI
def Play():
    Globals.scene = "game"


def Exit():
    global isRunning
    isRunning = False


# Opening splash screen ##################################################
btnPlay = Menu.Button(text = "Play", rect = (0, 20, 160, 60),
                      bg = Color.Gray, fg = Color.White,
                      bgr = Color.CornflowerBlue, tag = ("menu", None))
btnPlay.Left = window_width / 2 - btnPlay.Width / 2
btnPlay.Top = window_height / 2 - btnPlay.Height / 2
btnPlay.Command = Play

btnExit = Menu.Button(text = "Exit", rect = (0, 0, 160, 60),
                      bg = Color.Gray, fg = Color.White,
                      bgr = Color.CornflowerBlue, tag = ("menu", None))


btnExit.Left = btnPlay.Left
btnExit.Top = btnPlay.Top + btnExit.Height + 6
btnExit.Command = Exit

menuTitle = Menu.Text(text = "Welcome to the RPG", color = Color.Red,
                      font = Font.Large)

menuTitle.Left, menuTitle.Top = window_width / 2 - menuTitle.Width / 2, 0

logo = Menu.Image(bitmap = logo_img)
logo.Left = window_width / 2 - logo.Width / 2
logo.Top = window_height / 2 - logo.Height / 2
#############################################################################



isRunning = True
# Start the game loop
while isRunning:
    # listen for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not Globals.dialog_open:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s and not Globals.dialog_open:
                Globals.camera_move = 2
                player.facing = "south" 
            elif event.key == pygame.K_a and not Globals.dialog_open:
                Globals.camera_move = 3
                player.facing = "east" 
            elif event.key == pygame.K_d and not Globals.dialog_open:
                Globals.camera_move = 4
                player.facing = "west" 

            if event.key == pygame.K_RETURN:
                if Globals.dialog_open:
                    # HANDLE NEXT PAGE OF OPEN DIALOG
                    if Globals.active_dialog.Page < len(Globals.active_dialog.Text) - 1:
                        Globals.active_dialog.Page += 1
                    else:
                        Globals.dialog_open = False
                        Globals.active_dialog.Page = 0
                        Globals.active_dialog = None
                        #UNPAUSE ANY PAUSED NPC'S
                        for npc in NPC.AllNPCs:
                            if not npc.Timer.Active:
                                npc.Timer.Start()

            else:
                # IF DIALOG ISN'T OPEN
                for npc in NPC.AllNPCs:
                    # IS PLAYER IN SPEECH BOUNDS
                    # PLAYER COORDS ARE BY TILE
                    # NPC COORDS ARE BY PIXEL
                    if (npc.world_map == Globals.current_map):
                        npc_x = npc.X / Globals.tile_size
                        npc_y = npc.Y / Globals.tile_size
                        if (player_x >= npc_x - 2 and player_x <= npc_x + 2 and player_y >= npc_y - 2 and player_y <= npc_y + 2):
                            # PLAYER IS NEXT TO AN NPC
                            if player.facing == "north" and npc_y < player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = False

                            elif player.facing == "south" and npc_y > player_y:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = False

                            elif player.facing == "east" and npc_x < player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = False

                            elif player.facing == "west" and npc_x > player_x:
                                Globals.dialog_open = True
                                Globals.active_dialog = npc.Dialog
                                npc.Timer.Pause()
                                npc.walking = False

                      

        elif event.type == pygame.KEYUP:
            # reset the move
            Globals.camera_move = 0

        # So far this only affects the menu buttons
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if event.button == 1 and Globals.scene == "menu": # LEFT CLICK
                #HANDLE BUTTON CLICK EVENTS
                for btn in Menu.Button.All:
                    if btn.Tag[0] == Globals.scene and btn.Rolling:
                        if btn.Command != None:
                            btn.Command() #DO BUTTON EVENT
                        btn.Rolling = False
                        break #EXIT LOOP
            # Debugging - how to check my current position
            #if (Globals.scene != "menu"):

            else:
                # for debugging, show me the character's position
                print("X:{} Y:{} / Camera X:{} Camera Y:{}".format(player_x, player_y, Globals.camera_x, Globals.camera_y)) 

 
    #Render Scene
    if Globals.scene == "game":

        if Globals.current_map == "world":

            #LOGIC
            if Globals.camera_move == 1:
                if not terrain_TS.Blocked_At((round(player_x), math.floor(player_y))):
                    Globals.camera_y += 100 * Globals.deltatime
            elif Globals.camera_move == 2:
                if not terrain_TS.Blocked_At((round(player_x), math.ceil(player_y))):       
                    Globals.camera_y -= 100 * Globals.deltatime
            elif Globals.camera_move == 3:
                if not terrain_TS.Blocked_At((math.floor(player_x), round(player_y))):
                    Globals.camera_x += 100 * Globals.deltatime
            elif Globals.camera_move == 4:
                if not terrain_TS.Blocked_At((math.ceil(player_x), round(player_y))):
                    Globals.camera_x -= 100 * Globals.deltatime

            player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / Globals.tile_size
            player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / Globals.tile_size


            #RENDER_GRAPHICS
            window.blit(Sky, (0,0))
            
            window.blit(terrain, (Globals.camera_x, Globals.camera_y))
            for npc in NPC.AllNPCs:
                if (npc.world_map == Globals.current_map):
                    npc.Render(window)

            # If the player has reached a town, castle or cave
            if (terrain_TS.Special_Location_At((round(player_x), round(player_y)))):

                    # Location of town
                if (round(player_x) == 5 and round(player_y) == 9) and Globals.current_map == "world":     #pos(5, 9)

                    Globals.current_map = "town"
                    # Set the starting position for the new map

                    player_x, player_y = 10, 10
                    Globals.camera_x, Globals.camera_y = 0, 0
                    
                    for npc in NPC.AllNPCs:
                        # if the NPC belones to the new map
                        if npc.world_map == Globals.current_map:
                            npc.Timer.Start()
                            npc.Walking = True
                        # Otherwise stop all other NPCs
                        else:
                            npc.Timer.Pause()
                            npc.walking = False
                        

        elif Globals.current_map == "town":

            #LOGIC
            if Globals.camera_move == 1:
                if not town_TS.Blocked_At((round(player_x), math.floor(player_y))):
                    Globals.camera_y += 100 * Globals.deltatime
            elif Globals.camera_move == 2:
                if not town_TS.Blocked_At((round(player_x), math.ceil(player_y))):       
                    Globals.camera_y -= 100 * Globals.deltatime
            elif Globals.camera_move == 3:
                if not town_TS.Blocked_At((math.floor(player_x), round(player_y))):
                    Globals.camera_x += 100 * Globals.deltatime
            elif Globals.camera_move == 4:
                if not town_TS.Blocked_At((math.ceil(player_x), round(player_y))):
                    Globals.camera_x -= 100 * Globals.deltatime

            player_x = (window_width / 2 - player_w / 2 - Globals.camera_x) / town_TS.Size
            player_y = (window_height / 2 - player_h / 2 - Globals.camera_y) / town_TS.Size



            #RENDER_GRAPHICS
            window.blit(Sky, (0,0))
            window.blit(town, (Globals.camera_x, Globals.camera_y))
            for npc in NPC.AllNPCs:
                if (npc.world_map == Globals.current_map):
                    npc.Render(window)


            # Change to map size !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if (round(player_x) >= 19):     #pos(5, 9)
                Globals.current_map = "world"
                print("change")
                player_x, player_y = 0,0
                Globals.camera_x, Globals.camera_y = Globals.tile_size * 6, 0
                for npc in NPC.AllNPCs:
                    if npc.world_map == Globals.current_map:
                    # Start all the NPCs in the world map
                        npc.Timer.Start()
                        npc.walking = True
                    else:
                    # stop all the other NPCs
                        npc.Timer.Start()
                        npc.walking = False
                        


        # For now we render the player in the center of the screen
        player.render(window, (window_width / 2 - player_w / 2,
                               window_height / 2 - player_h / 2))


        if Globals.dialog_open:
            window.blit(Dialog_Background, (window_width / 2 - Dialog_Background_Width / 2, window_height - Dialog_Background_Height))


            #Draw Dialog Text
            if Globals.active_dialog != None:
                lines = Globals.active_dialog.Text[Globals.active_dialog.Page]

                for line in lines:
                    # DRAW TEXT TO SCREEN
                    window.blit(Font.Default.render(line, True, Color.White), (130, (window_height - Dialog_Background_Height) + 5 + (lines.index(line)) * 25))




    # PROCESS MENU
    elif Globals.scene == "menu":
        window.fill(Color.Fog)

        logo.Render(window)
        menuTitle.Render(window)


        for btn in Menu.Button.All:
            if btn.Tag[0] == "menu":
                btn.Render(window)



        
    clock.tick()
    show_fps()

    #clock.tick(100)

    pygame.display.update()
    count_fps()

                             
