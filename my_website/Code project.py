# -*- coding: utf-8 -*-
import pipi
#This is a comment
def pipi():
    print("Pipi was bored and decided to sneak into Dry Town during closing hours.")
    time.sleep(3)
    print('         .__       .__  ')
    print( ' ______ |__|_____ |__|  ')
    print (' \____ \|  \____ \|  |  ')
    print (' |  |_> >  |  |_> >  |  ')
    print('  |   __/|__|   __/|__|   ')
    print('  |__|      |__|      ')
    print('You are enjoying your time, you spot an officer from the top of the big red slide')
    time.sleep(1)
    choice=raw_input('You are paranoid. Do you make your way toward the lagoon?(Y/N)')
    while choice == 'Y':
        print('You make your way into the lagoon and dive in')
        time.sleep(1)
        choice=raw_input('Do consider the snack bar?(Y/N)')
    print('Time to escape')
    time.sleep(1)
    choice=raw_input('You get in and make noise with the splash. What do you do?(Dive in/Make a run for it Away)')
    while choice != 'Run Away' and choice !='Dive in':
        choice=raw_input('Invalid Answer. Try again(Run Away/Attack Them)')
    if choice == 'Dive in':
        print('officer approaches and you hide under the bridge above the lagoon')
        time.sleep(1) 
        print('You are caught and now you have to pay a fine.')
        time.sleep(1)
        print('You are dead')
    else: #you chose Run Away
        choice=raw_input('You successfully ran away. Where to go next?( You discreetly make your way towards the snack bar):')
        while choice != 'Snack bar':
            choice=raw_input('Invalid Answer.Try again. (Snack bar/Shack)')
        if choice == 'Snack Bar':
            print('You are hidden in the snack bar.')
            time.sleep(1)
            print('The officer is near and you and you grab a hot dog')
            time.sleep(1)
            print('You are now armed and ready to make a run for it.')
            time.sleep(1)
            print('You throw the hot dog down to distract the officer')
            time.sleep(1)
            print('No one is getting fine ')
            
            
