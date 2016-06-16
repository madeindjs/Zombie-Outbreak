# Zombie-Outbreak

A Zombie Apocalypse simulator created in Python.

## Synopsis

Did you now how many time the humanity survive in a Zombie Apocalypse? Do you think Humans can kill all zombies to prevent infection? I don't know too but **Zombie Outbreak** can say it!

## Algorithm

The scene take place in a 80*10 place in your terminal represent the entire world. Each turn represent 6 hours in a day. This is a classic turn:

1. Each Zombie / Humans move orthogonally like this:

           ^
           |  
       <-- Z -->
           |
           V


2. If there are humans in 


## Developpement

Developped only in Python from an originally idea of ..... in winter 2012. Forked and updated in June 2016.

Created:  

             Winter 2012

Description:
          
         'Zombie-Simulator' features a 10 by 10 grid which represents a bustling city
         inhabited by humans. The program then runs an algorithm that predicts
         what would happen to the city if a zombie outbreak were to occur. 
         
         The program is divided into two parts:
         
         Part A: 
         
            The user is able to pick how many turns they would like to run the algorithm for.
            An intial starting populace of humanity in the city is mapped out.
            During Turn 0, a single zombie is spawned randomly in one of the grids in the city.
            The program then outputs the final outcome after an n number of turns have passed.
            
         Part B:
         
            The user can choose to spawn an n number of zombies in a random location in the city.
            The program runs the algorithm and determines the number of turns it took for either
            humanity or the zombies to be completely wiped out.

Zombie Algorithm:

         Every zombie alive, during a single turn, goes through this algorithm once.
         
         The algorithm can sorted into three steps:
                i) Movement: the zombie, in a randomized fashion, moves one block through the city.
               ii) Encounter: if the zombie encounters a human iii) is initiated.
                              if this does not occur, the zombie ends its turn.
              iii) Result: The result of the encounter between a zombie and a human is
                           determined randomly and can end in one of three way:
                               1) the zombie is eliminated
                               2) the human is eliminated
                               3) the human is turned into a zombie
         
         
Instructions:

         To use, simply run the run the program on PythonIDLE (as it has 
         a larger screen for text to show up) and follow the instructions.
         
