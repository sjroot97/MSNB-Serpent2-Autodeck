#./drum.py
def card(deg):
    with open('cards/drum.txt','w') as drumcards:
        drumcards.write(f'% Control drum absorber pads, numbered clockwise from 9 o clock\n')
        drumcards.write(f'surf 80 pad -45.05 0 16 17 {deg-45} {deg+45} % drum 1\n')
        drumcards.write(f'surf 81 pad -31.8551605 31.8551605 16 17 {deg-0} {deg+90} % drum 2\n')
        drumcards.write(f'surf 82 pad 0 45.05 16 17 {deg+45} {deg+135} % drum 3\n')
        drumcards.write(f'surf 83 pad 31.8551605 31.8551605 16 17 {deg+90} {deg+180} % drum 4\n')
        drumcards.write(f'surf 84 pad 45.05 0 16 17 {deg+135} {deg+225} % drum 5\n')
        drumcards.write(f'surf 85 pad 31.8551605 -31.8551605 16 17 {deg+180} {deg+270} % drum 6\n')
        drumcards.write(f'surf 86 pad 0 -45.05 16 17 {deg-135} {deg-45} % drum 7\n')
        drumcards.write(f'surf 87 pad -31.8551605 -31.8551605 16 17 {deg-90} {deg+0} % drum 8\n')
        