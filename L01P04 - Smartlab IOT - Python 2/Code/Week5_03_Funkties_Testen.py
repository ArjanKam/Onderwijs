def serieWeerstand(weerstanden):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + item
    return rVervanging

def parallelWeerstand(weerstanden):
    rVervanging = 0
    for item in weerstanden:
        rVervanging = rVervanging + 1/item
    return 1/rVervanging

if __name__ == "__main__":
    assert serieWeerstand([5,5]) == 10
    assert serieWeerstand([5,5,20]) == 30
    assert parallelWeerstand([5,5]) == 2.5
