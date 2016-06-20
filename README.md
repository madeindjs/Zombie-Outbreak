# Zombie-Outbreak

A Zombie Apocalypse simulator created in Python.

## Synopsis

Did you now how many time the humanity survive in a Zombie Apocalypse? Do you think Humans can kill all zombies to prevent infection? I don't know too but **Zombie Outbreak** can say it!

## Algorithm

The scene take place in a 80*10 place in your terminal represent the entire world. Each turn represent 6 hours in a day. This is a classic turn:

1. Each Zombie / Humans move orthogonally (top, bottom, left & right):
2. If there are humans in a same area than a Zombie, the zombie will attack him. At this point, there are 1/2 chance that:
      * **zombie kill human**. In this case, the human transform in a zombie
      * **human kill zombie**. In this case, the zombie is dead
3. if there are at least two humans in the same area and no zombie, humans **have a sex**. At this point, there are 1/3 chance that a new human birth

## Launch

    sudo pip install clint #for terminal color support
    git clone https://github.com/a-tamang/Zombie-Outbreak
    python zombie-outbreak


## Developpement

Developped only in Python from an originally idea of [Ashish Tamang](https://github.com/a-tamang) in winter 2012. Forked and updated in June 2016 by [Alexandre Rousseau](https://github.com/madeindjs).

### Unit Test

You can run units test with this command

    python tests.py