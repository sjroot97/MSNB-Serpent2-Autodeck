#./makedeck.py
import datetime,os
import salt, drum
now =datetime.date.today()

deg = 112#float(input('')), take input to interact with Bash
enrich = 19.75 #percentage
folder = f'./results/{deg}'

if not os.path.exists(folder):
    os.makedirs(folder)

print(folder)
salt.card(enrich)
drum.card(deg)

with open(f'{folder}/MSNB', 'w') as deck,\
     open('cards/cell.txt','r') as cell,\
     open('cards/surface.txt','r') as surface,\
     open('cards/drum.txt','r') as drum,\
     open('cards/salt.txt','r') as salt,\
     open('cards/material.txt','r') as material,\
     open('cards/physics.txt','r') as physics,\
     open('cards/plot.txt','r') as plot:
    
    deck.write(f'set title "Root MSNB at {deg} Degrees, {enrich} percent enrichment"\n')
    deck.write(f'%Revised {now}\n%\n')

    for line in cell:
        deck.write(line)
    for line in surface:
        if not 'WRITE_PADS' in line:
            deck.write(line)
        else:
            for l in drum:
                deck.write(l)
    for line in salt:
        deck.write(line)
    for line in material:
        deck.write(line)
    for line in physics:
        deck.write(line)
    for line in plot:
        deck.write(line)