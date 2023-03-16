# r1 en r2 zijn van het datatype int of float
def berekenSerieWeerstand( r1, r2 ):
    rVervanging = r1 + r2
    return rVervanging

def berekenParallelWeerstand( r1, r2):
    rVervanging = r1 * r2 / (r1 + r2)
    return rVervanging
    
antwoord = berekenParallelWeerstand( 42, 66 )
antwoord = berekenParallelWeerstand( antwoord, 78 )
antwoord = berekenParallelWeerstand( antwoord, 3 )
antwoord = berekenParallelWeerstand( antwoord, 5 )
print(antwoord)

