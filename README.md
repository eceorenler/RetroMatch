# RetroMatch

Retro Match is a pixel match-3 puzzle game developed with Python and Pygame.
The player swaps adjacent alien tiles to create matches of three or more and score as many points as possible before the timer runs out.


---


### Features

- Retro inspired visual style
- Match-3 puzzle gameplay
- Tile pop animation effects
- Score and countdown timer system
- Shuffle system when no valid moves remain
- Menu scene, gameplay scene, and game over scene
- Sound effects


### Assets
- All game pixel art assets were created by the developer.
- The font and sound effects were obtained from external free resources and are used for educational purposes only.


---


### How to Run
1. Install Python
2. Install Pygame:

```text
pip install pygame
```

3. Run the game:

```text
python main.py
```


### How to Play

- Click two adjacent alien tiles to swap them
- Match 3 or more identical aliens to gaim points.
- The game lasts for 60 seconds
- Try to achive the highest score possible before time is up.


### Controls

| Input | Action |
|---|---|
| Mouse Click | Select and swap tiles |
| Enter | Start the game |
| R | Restart after game over |
| ESC | Quit the game |


---


### Technologies Used

Python and Pygame

### Project Structure

```text
core/
    sceneManager.py

game/
    board.py
    tile.py

scenes/
    menuScene.py
    gameScene.py
    gameOver.py

assets/
    sprites/
    sounds/
    fonts/

main.py
settings.py
```
