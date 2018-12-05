import pygame

pygame.init()

def Load_Texture(file, Size):
    # Loads the images for each tile type
    bitmap = pygame.image.load(file)
    bitmap = pygame.transform.scale(bitmap, (Size, Size))
    # And then draws it on the surface
    surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
    surface.blit(bitmap, (0,0))
    return surface



class Tiles():

    def __init__(self):

        self.Size = 32

        # Special locations are towns, cities, caves, 
        self.Special_Location = []
        self.Special_Location_Types = ["7", "8", "9"]

        # Water, mountains, stone wall, 
        self.Blocked = []
        self.Blocked_Types = ["3","4", "10", "13"]

        Grass = Load_Texture("graphics\\grass.png", self.Size)
        Stone = Load_Texture("graphics\\stone.png", self.Size)
        Water = Load_Texture("graphics\\water.png", self.Size)
        Mountain = Load_Texture("graphics\\mountain.png", self.Size)
        Forest = Load_Texture("graphics\\forest.png", self.Size)
        Hill = Load_Texture("graphics\\hill.png", self.Size)
        Cave = Load_Texture("graphics\\cave.png", self.Size)
        Town = Load_Texture("graphics\\town.png", self.Size)
        Castle = Load_Texture("graphics\\castle.png", self.Size)
        StoneWall = Load_Texture("graphics\\stone_wall.png", self.Size)
        Brick = Load_Texture("graphics\\brick.png", self.Size)
        Rock = Load_Texture("graphics\\rock.png", self.Size)        

        self.Texture_Tags = {"1" : Grass, "2" : Stone, "3" : Water, "4" : Mountain, "5" : Forest, "6" : Hill, "7" : Cave, "8" : Town, "9" : Castle, "10" : StoneWall, "11" : Brick, "12" : Rock}
        self.Tile_Names = {"1" : "Grass", "2" : "Stone", "3" : "Water", "4" : "Mountain", "5" : "Forest", "6" : "Hill", "7" : "Cave", "8" : "Town", "9" : "Castle", "10" : "Stone Wall", "11" : "Brick", "12" : "Rock"}
  


    def Blocked_At(this, pos):
        if list(pos) in this.Blocked:
            return True
        else:
            return False

    def Special_Location_At(this, pos):
        if list(pos) in this.Special_Location:
            return True
        else:
            return False



    
    
  
