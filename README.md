# Group7_FinalProject_Frogger

This is the culmination of a trimesters class of Advanced Programming with python, a re-creation of Frogger using graphics.py.

The goal was to create an almost fully fledged version of the game using only graphics.py and the base libraries Python provides.


The game allows the user to control the frog, the player evade cars, hitch a ride from some turtles and jump on logs to avoid 
sinking, with the end goal of reaching the swamp to safety. The game also has a scoring system, which takes in account 
the highest score made in the local computer, which can register your name, the time spent, and the score obtained 
during the time played.

Each object created is designated in its own classes: Turtles, Logs, Cars, the Frog, and the background itself.
Almost all of these are made with a hitbox, which registers the collision between the frog and the objects;
the cars are programmed to when they come in contact with the frog, the turtles and logs are utilize the same
mechanic to determine if the frog is on them or not, as there are safe zones where the frog can stand on, 
these being some of them, once outside these zones the frog or if hit by a car, a player must try again.
