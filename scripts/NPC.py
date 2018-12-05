import pygame, random
from scripts.Timer import Timer
from scripts.globals import Globals
from scripts.textures import *

pygame.init()

def get_faces(sprite):
    faces = {}

    size = sprite.get_size()
    tile_size = (int(size[0] /2), int(size[1] / 2))

    south = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    south.blit(sprite, (0, 0), (0, 0, tile_size[0], tile_size[1]))
    faces["south"] = south

    north = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    north.blit(sprite, (0, 0), (tile_size[0], tile_size[1], tile_size[0], tile_size[1]))
    faces["north"] = north

    east = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    east.blit(sprite, (0, 0), (tile_size[0], 0, tile_size[0], tile_size[1]))
    faces["east"] = east

    west = pygame.Surface(tile_size, pygame.HWSURFACE|pygame.SRCALPHA)
    west.blit(sprite, (0, 0), (0, tile_size[1], tile_size[0], tile_size[1]))
    faces["west"] = west

    return faces


def MoveNPC(npc):
    npc.facing = random.choice(("south", "north", "east", "west"))
    npc.walking = random.choice((True, False))


class Dialog:
    def __init__(self, text):
        self.Page = 0
        self.Text = text # [("hello friend", "how are you"), ("This is the next page"), ("this is another mofo page")]

class NPC:

    AllNPCs = []

    def __init__(self, name, pos, world, tiles, dialog, sprite):
        self.Name = name
        self.X = pos[0]
        self.Y = pos[1]
        self.Dialog = dialog
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.walking = False
        self.Timer = Timer(2)
        self.Timer.OnNext = lambda: MoveNPC(self)
        self.Timer.Start()
        #NPC has access to their map tiles
        self.tiles = tiles
        #print (tiles)

        self.LastLocation = [0, 0]
        self.world_map = world

        # GET NPC FACES
        self.facing = "south"
        self.faces = get_faces(sprite)

        # PUBLISH
        NPC.AllNPCs.append(self)

    def Render(self, surface):
        global tiles
        self.Timer.Update()
        if self.walking:
            move_speed = 25 * Globals.deltatime  # 75 * Globals.deltatime
            if self.facing == "south":
                self.Y += move_speed
            elif self.facing == "north":
                self.Y -= move_speed
            elif self.facing == "east":
                self.X -= move_speed
            elif self.facing == "west":
                self.X += move_speed

            # BLOCK TILE NPC IS STANDING ON
            # took out the tile size
            location = [round(self.X / Globals.tile_size), round(self.Y / Globals.tile_size)]
            if self.LastLocation in self.tiles: #.Blocked or self.LastLocation in tiles.Special_Location:
                self.tiles.remove(self.LastLocation)

            if not location in self.tiles: #.Blocked:
                self.tiles.append(location)
                self.LastLocation = location

        surface.blit(self.faces[self.facing], (self.X + Globals.camera_x, self.Y + Globals.camera_y))

class Male1(NPC):

    def __init__(self, name, pos, world, tiles, dialog = None):
        
        super().__init__(name, pos, world, tiles, dialog, pygame.image.load("C:\\DATA\\python\\games\\rpg_dw\\graphics\\NPC\\male1.png"))
        
