# Talana Kombat JRPG
Small challenge implementation that aims to narrate actions in
a mini combat game using POO and python scripts.

## Python version
I'm using python 3.9 for this project but it should work with python>=3.5

## Instructions for development:

#### 1. Create virtualenv:
```
user@pc:/home$ virtualenv -p=python3 venv
```
#### 2. activate virtualenv:
```
user@pc:/home$ source venv/bin/activate
```
#### 3. Clone the repository:
```
git clone git@github.com:ChronoFrank/TalanaKombat.git 

or 

git clone https://github.com/ChronoFrank/TalanaKombat.git
```
#### 4. Install dependencies:
```
(venv) cd TalanaKombat
pip install -r requirements.txt
```
#### 5. run script:
```
(venv) Talana
```

# The challenge
Talana Kombat is a game where 2 characters fight each other to the death.
Each character has 2 special hits that are executed with 
a combination of moves + 1 hit button.

## Allowed control buttons
W = Up, A = Right, S = Left, D = Right, P = Punch, K = Kick <br>

## Game rules
The player who sent a smaller combination of buttons (movement + hits) starts attacking, in case of a tie, the player with the least moves starts, if they tie again, the one with the least hits starts, if there is a tie again, the player 1 starts ( Total player 2 is always from the little brother)

The entire combat sequence for each player is delivered at once (consolidated into a json)
Each character has 6 Energy Points

-A character dies when his energy reaches 0 and immediately ends the fight
- Tony is player 1, he always attacks to the right (and doesn't change sides)
- Arnaldor is player 2, he always attacks to the left (and does not change sides)
- Characters attack each other one at a time JRPG style, taking turns until one is
defeated, hits cannot be blocked, they are assumed to always be effective.

The data arrives as a json with movement and hit buttons that are correlated for each play

The movements can be a string with a maximum length of 5 (it can be empty)

Hits can be a single button max (can be empty)

The hit button is assumed to be right after the move sequence, ie AADSD + P is a Taladoken (it moved backwards 2 times before); DSDAA + P are moves plus a fist