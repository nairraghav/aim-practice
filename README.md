# aim-practice
An aiming game created with the pygame python library

## Game Rules
When the game is run, you are immediately thrown into a game where targets are randomly generated within the game screen.
The goal is to click on the targets. When you click on a target, you will be awarded a point and the target should
re-generate somewhere else. If you do not click on the target before the target disappears on its own, it will disappear
and re-generate in a new location. You should be able to tell if the game received the click via a ding sound cue. 
Similarly, if time has passed for a target, you will hear a whoosh sound. 

A game has concluded once all the targets have shown up and been clicked or missed. The end of the game will generate
a small statistics board with a chance to replay.

## Game Settings
For any settings that you would like to change, please update `aim_practice.py` and re-run the game. I have noted which
parts of the file you will want to change. I have plans to incorporate this within the game itself soon but for now, you
will need to touch the source code

### Targets Per Game
Each game has a max of 5 targets that you can hit
```python
TARGETS_PER_GAME = 5
```

### Max Time Per Target
Each target stays up for a max of 2 seconds before it marks it as a miss
```python
TIME_BETWEEN_TARGETS = 2000  # milliseconds
```

## How To Run
I have included a Makefile to make it easy to install dependencies and run the game

### Install Dependencies
```bash
make install
```

### Run Game
```bash
make run
```

## To Do
* Start the game at a settings screen instead of directly in the game
    * User should have the option to select targets per game
    * User  should have the option to select time between targets
* When the game ends, user should be able to update settings as well as see stats
* Infinite Mode
    * User should be able to continuously play the game without it ending unless the user manually quits
        * If game is quit (without exiting), stats are shown 
* Allow user to disable sound
* Fix Stats Bug
    * If you don't hit a target on time but don't click (and hit all other targets), accuracy shows as 100%
    


