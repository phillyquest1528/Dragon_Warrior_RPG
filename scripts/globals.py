
class Globals:
# Global variables for the game
# Scene values are: 'menu', 'game'
#
# Date: November 18, 2018
# - Added a map variable to change the current map
# - should use a stack to allow user to easily return to previous map


    camera_x =0
    camera_y =0
    camera_move =0
    scene = "menu"

    current_map = "world"
    
    deltatime = 0

    dialog_open = False
    active_dialog = None

    tile_size = 32

    last_position_x, last_position_y = 0, 0
