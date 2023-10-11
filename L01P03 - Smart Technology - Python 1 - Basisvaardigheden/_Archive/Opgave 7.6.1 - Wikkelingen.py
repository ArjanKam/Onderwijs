def transformUout(u_in, n_in, n_out):
    if n_in == 0:
        return 0
    return n_out/n_in * u_in


if __name__ == "__main__":
    print("Begin test")
    assert transformUout(20, 100, 200) == 40
    assert transformUout(20, 400, 100) == 5
    assert transformUout(-20, 400, 100) == -5
    assert transformUout(100, 0, 100) == 0
    #maak deze testen ook voor de andere functies
    
    
    print("All test ok")
    
    
    
    