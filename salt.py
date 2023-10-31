#./salt.py
def uranium(enrich):
    total = 1.40246e-2 + 5.69859e-2
    u235 = total*enrich/100
    u238 = total - u235
    return '{:.5e}'.format(u235), '{:.5e}'.format(u238)

def card(enrich):
    u235, u238 = uranium(enrich)
    with open('cards/salt.txt','w') as saltcards,\
         open ('cards/salttemps.txt','r') as temps:

        saltcards.write('%_____Material Cards_____\n')
        saltcards.write('%LiF-NaF-KF-UF4\n')
        saltcards.write(f'%18 mole percent UF4 at {enrich} percent enrichment\n')
        
        for line in temps:
            saltcards.write(line)
            with open('cards/flinak.txt','r') as flinak:
                for l in flinak:
                    saltcards.write(l)
            saltcards.write(f'92235.06c {u235}\n')
            saltcards.write(f'92238.06c {u238}\n')