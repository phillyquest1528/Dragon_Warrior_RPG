import pygame

# Date: November 10, 2018
# Changing the Tiles class to be a map class with a tiles method


pygame.init()

class Tiles:

    Size = 32

    Blocked = []

    Blocked_Types = ["3","4"]


    def Blocked_At(pos):
        if list(pos) in Tiles.Blocked:
            return True
        else:
            return False



    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0,0))
        return surface


    Grass = Load_Texture("graphics\\grass.png", Size)
    Stone = Load_Texture("graphics\\stone.png", Size)
    Water = Load_Texture("graphics\\water.png", Size)
    Mountain = Load_Texture("graphics\\mountain.png", Size)
    Forest = Load_Texture("graphics\\forest.png", Size)
    Hill = Load_Texture("graphics\\hill.png", Size)
    Cave = Load_Texture("graphics\\cave.png", Size)
    Town = Load_Texture("graphics\\town.png", Size)
    Castle = Load_Texture("graphics\\castle.png", Size)
    
    Texture_Tags = {"1" : Grass, "2" : Stone, "3" : Water, "4" : Mountain, "5" : Forest, "6" : Hill, "7" : Cave, "8" : Town, "9" : Castle}
    Tile_Names = {"1" : "Grass", "2" : "Stone", "3" : "Water", "4" : "Mountain", "5" : "Forest", "6" : "Hill", "7" : "Cave", "8" : "Town", "9" : "Castle"}
    
