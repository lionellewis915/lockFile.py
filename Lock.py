'''
Created by: Lionel Lewis

Simple locking algorithm that allows the user
to set a pin and lock a file.

The file will not unlock until the the correct pin is entered.
'''

locked = False
pin = '0000'
numUnlock = 0

userChoice = 'Y'

def lock():
    global locked
    locked = True
    print('Locked')
    print()


def unlock():
    global locked
    global numUnlock
    userPin = input ('Enter PIN or q to quit')
    print()

    while (userPin != pin and userPin != 'q' ):
        userPin = input('Enter PIN')
        print()

        if userPin != pin:
            numUnlock = numUnlock + 1

    if userPin == pin:
        locked = False


def setPIN():
    global pin
    pin = input ('Enter New PIN')
    print()


def status():
    print ("System Lock is {0} PIN is {1} Number of incorrect unlocks is {2}".format(locked, pin, numUnlock))
    print()

def displayMenu():
    print('1 - Lock')
    print('2 - Set PIN')
    print('3 - Unlock')
    print('4 - Status')
    print('5 - Quit')
    print()

while userChoice != 5:
    displayMenu()
    userChoice = int(input('Enter Choice'))
    print()

    if userChoice == 1:
        lock()

    elif userChoice == 2:
        setPIN()

    elif userChoice == 3:
        unlock()

    elif userChoice == 4:
        status()

