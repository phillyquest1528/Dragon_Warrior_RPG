# Import Python libraries and scripts
import pygame, sys, math
from scripts.UltraColor import *
from scripts.textures import *

# Always got to initialize pygame
pygame.init()

# Save the newly created map
def export_map(file):
    map_data = ""

    # Get map dimensions
    max_x = 0
    max_y = 0

    for t in tile_data:
        if t[0] > max_x:
            max_x = t[0]
        if t[1] > max_y:
            max_y = t[1]

    # Save Map Tiles
    for tile in tile_data:
        map_data = map_data + str(int(tile[0] / NewMap.Size)) + "," + str(int(tile[1] / NewMap.Size)) + ":" + tile[2] + "-"

    # Save Map Dimensions
    map_data = map_data + str(int(max_x / NewMap.Size)) + "," + str(int(max_y / NewMap.Size))

    # Write Map File
    with open(file, "w") as mapfile:
        mapfile.write(map_data)



def load_map(file):
    global tile_data
    with open(file, "r") as mapfile:
        map_data = mapfile.read()

    map_data = map_data.split("-")

    map_size = map_data[len(map_data) - 1]
    map_data.remove(map_size)
    map_size = map_size.split(",")
    map_size[0] = int(map_size[0]) * NewMap.Size
    map_size[1] = int(map_size[1]) * NewMap.Size

    tiles = []

    for tile in range(len(map_data)):
        map_data[tile] = map_data[tile].replace("\n", "")
        tiles.append(map_data[tile].split(":"))

    for tile in tiles:
        tile[0] = tile[0].split(",")
        pos = tile[0]
        for p in pos:
            pos[pos.index(p)] = int(p)

        tiles[tiles.index(tile)] = [pos[0] * NewMap.Size, pos[1] * NewMap.Size, tile[1]]

    tile_data = tiles



window = pygame.display.set_mode((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Map Editor")
clock = pygame.time.Clock()

# Create Tiles object
NewMap = Tiles()


txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

# Set the dimensions of the map to create.  50 x 50.
width_in_tiles, height_in_tiles = 20, 20
map_width, map_height = width_in_tiles * NewMap.Size, height_in_tiles * NewMap.Size

selector = pygame.Surface((NewMap.Size, NewMap.Size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_move = 0

brush = "2"



# Initialize Default Map
for x in range(0, map_width, NewMap.Size):
    for y in range(0, map_height, NewMap.Size):
        tile_data.append([x, y, "1"])

isRunning = True

while isRunning:
    # Wait for the user event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:

            # MOVEMENT
            if event.key == pygame.K_w:
                camera_move = 1
            elif event.key == pygame.K_s:
                camera_move = 2
            elif event.key == pygame.K_a:
                camera_move = 3
            elif event.key == pygame.K_d:
                camera_move = 4

            # BRUSHES
            if event.key == pygame.K_1:
                print (NewMap.Tile_Names)
                selection = input("Brush Tag: ")
                print("{0} brush selected".format(NewMap.Tile_Names[selection]))
                brush = selection

            # SAVE MAP
            if event.key == pygame.K_2:
                name = input("Map Name: ")
                export_map(name + ".map")
                print("Map Saved Successfully")

            #LOAD MAP
            elif event.key == pygame.K_l:
                name = input("Map Name: ")
                load_map("maps//" + name + ".map")
                print("Map Successfully Loaded")

        elif event.type == pygame.KEYUP:
            camera_move = 0

        if event.type == pygame.MOUSEMOTION:
            # Get the location of the mouse.  Set the tile.
            mouse_pos = pygame.mouse.get_pos()
            mouse_x = math.floor(mouse_pos[0] / NewMap.Size) * NewMap.Size
            mouse_y = math.floor(mouse_pos[1] / NewMap.Size) * NewMap.Size

        if event.type == pygame.MOUSEBUTTONDOWN:
            # User selects a tile.
            #tile = [mouse_x - camera_x, mouse_y - camera_y, brush] # Keep this as a list

            #print("x:{0} y:{1}".format(int((mouse_x - camera_x) / Tiles.Size),int((mouse_y - camera_y) / Tiles.Size)))

            #coordinates show the tile size.  need to divide by tile size to get position
            if (mouse_x - camera_x < 0 or mouse_x - camera_x >= map_width):
                print("Out of bounds - x")

            elif (mouse_y - camera_y < 0 or mouse_y - camera_y >= map_height):
                print("Out of bounds - y")

            # The selected tile is within bounds
            else:
                try:
                    index = 0
                    x_pos, y_pos = int((mouse_x - camera_x) / NewMap.Size), int((mouse_y - camera_y) / NewMap.Size)
                    if (x_pos == 0):
                        index = y_pos
                    elif (y_pos == 0):
                        index = x_pos * width_in_tiles
                    else:
                        index = x_pos * width_in_tiles + y_pos

                    tile_data.pop(index)
                    tile_data.insert(index, [mouse_x - camera_x, mouse_y - camera_y, brush])
                except:
                    print("Error")

                #map_pos = int(str(int((mouse_x - camera_x) / Tiles.Size)) + str(int((mouse_y - camera_y) / Tiles.Size)))
                # Make sure the position is within the map
                #if map_pos <= len(tile_data):
                #    tile_data.pop(map_pos)
                #    tile_data.insert(map_pos, tile)
                #    print("New tile...")
            # User selected outside the map area
            #except:
                #print("Out of range")
                
#            print("{0}{1}".format(int((mouse_x - camera_x) / Tiles.Size), int((mouse_y - camera_y) / Tiles.Size)))            

##            if tile in tile_data:
##
##
##                if not brush == "r":
##                    print("Index of tile_data: {}".format(tile_data.index(tile)))

#                else:
#                    print("Index of tile_data: {}".format(tile_data.index(tile)))

                



            # Is a tile already placed here?
##            found = False
##            for t in tile_data:
##                print("t0:{} tile0:{}".format(t[0],tile[0]))
##                print("t1:{} tile1:{}".format(t[1],tile[1]))
##                if t[0] == tile[0] and t[1] == tile[1]:
##                    found = True
##                    print("Going to break")
##                    break
##
##
            # If this tile space is empty
##            if not found:
##                if not brush == "r":
##                    print("There is no tile here")
##                    tile_data.append(tile)
##
            # If this tile space is not empty
##            else:
##                # Are we using the rubber tool?
##                if brush == "r":
##                    # Remove tile
##                    print("remove?")
##                    for t in tile_data:
##                        if t[0] == tile[0] and t[1] == tile[1]:
##                            tile_data.remove(t)
##                            print("Tile Removed")
##
##                else:
##                    # Sorry! A tile is already placed here
##                    print("A tile is already placed here!")

    # LOGIC
    if camera_move == 1:
        camera_y += NewMap.Size
    elif camera_move == 2:
        camera_y -= NewMap.Size
    elif camera_move == 3:
        camera_x += NewMap.Size
    elif camera_move == 4:
        camera_x -= NewMap.Size

    # RENDER GRAPHICS
    window.fill(Color.Blue)

    # Draw Map
    for tile in tile_data:
        try:
            window.blit(NewMap.Texture_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
        except:
            pass

    # Draw Tile Highlighter (Selector)
    window.blit(selector, (mouse_x, mouse_y))


    pygame.display.update()

    #clock.tick(60)
    clock.tick(10)
    
pygame.quit()
sys.exit()
                




                

            
