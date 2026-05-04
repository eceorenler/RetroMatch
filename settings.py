#Window
WINDOW_WIDTH  = 480
WINDOW_HEIGHT = 700
FPS   = 60
TITLE = "Retro Match"

# Color Palette
GB_DARKEST  = (15,  56,  15)
GB_DARK     = (48,  98,  48)
GB_LIGHT    = (139, 172, 15)
GB_LIGHTEST = (155, 188, 15) 

#BlackScreen
SCREEN_X = 52
SCREEN_Y = 170
SCREEN_W = 290
SCREEN_H = 290

#Grid
GRID_COLS  = 5
GRID_ROWS  = 5
TILE_TYPES = 5

#Automatically calculate tile size
TILE_SIZE = min(SCREEN_W // GRID_COLS, SCREEN_H // GRID_ROWS)

#Starting point of the grid to be centered
GRID_X = SCREEN_X + (SCREEN_W - TILE_SIZE * GRID_COLS) // 2
GRID_Y = SCREEN_Y + (SCREEN_H - TILE_SIZE * GRID_ROWS) // 2

#Game duration and scoring
GAME_DURATION = 60 
WIN_SCORE     = 1000
MATCH_POINTS  = 100 