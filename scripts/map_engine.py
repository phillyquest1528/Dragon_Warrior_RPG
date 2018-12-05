import pygame
from scripts.textures import *

# Loading the map
# made up of tiles

class Map_Engine:


    #blitting is drawing
    # we draw the surface onto the window
    def add_tile(this, tile, pos, addTo, tileSet):
        #with tile size
        addTo.blit(tile, (pos[0] * tileSet.Size, pos[1] * tileSet.Size))


    def load_map(this, file, tileSet):

        # map format is x, y: tileCode - (dash delimiter)
        with open(file, "r") as mapfile:
            map_data = mapfile.read()

        #split into tiles
        map_data = map_data.split("-")

        map_size = map_data[len(map_data) - 1]
        # remove the last record, should be map size
        map_data.remove(map_size)
                
        map_size = map_size.split(",")
        
        map_size[0] = int(map_size[0]) * tileSet.Size
        map_size[1] = int(map_size[1]) * tileSet.Size

        tiles = []

        for tile in range(len(map_data)):
            # get rid of any newlines
            map_data[tile] = map_data[tile].replace("\n", "")
            #split into coordinates and brush
            tiles.append(map_data[tile].split(":"))

        for tile in tiles:
            # split the x and y
            tile[0] = tile[0].split(",")
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)
            # all this formatting, cast to integer, tiles array has position and tile type
            tiles[tiles.index(tile)] = (pos, tile[1])

        #Create the surface
        mySurface = pygame.Surface(map_size, pygame.HWSURFACE)
                
        for tile in tiles:
            # the code should match one of the tile types
            if tile[1] in tileSet.Texture_Tags:
                # draw this 
                this.add_tile(tileSet.Texture_Tags[tile[1]], tile[0], mySurface, tileSet)


    # add code to inlclude special spots such as towns and castles
            if tile[1] in tileSet.Special_Location_Types:
                tileSet.Special_Location.append(tile[0])
                
            # add the position of blocked types
            if tile[1] in tileSet.Blocked_Types:
                tileSet.Blocked.append(tile[0])

        # this show the two different sets of tiles
        #print(tileSet.Blocked)
        return mySurface

