from ppt import jugada_ppt, partida_ppt

def test_jugada():
    assert jugada_ppt("Piedra", "Tijera") == 1
    assert jugada_ppt("Tijera", "Piedra") == -1
    assert jugada_ppt("Tijera", "Tijera") == 0
    assert jugada_ppt("Papel", "Tijera") == -1

def test_partida():
    l1 = ["Piedra", "Piedra", "Piedra"]
    l2 = ["Papel", "Papel", "Papel"]
    assert partida_ppt(l1, l2) == -3
    l1 = ["Piedra", "Piedra", "Tijera"]
    l2 = ["Papel", "Piedra", "Papel"]
    assert partida_ppt(l1, l2) == 0
    l1 = ["Tijera", "Papel", "Tijera"]
    l2 = ["Papel", "Piedra", "Papel"]
    assert partida_ppt(l1, l2) == 3
    l1 = ["Piedra", "Papel", "Tijera"]
    l2 = ["Papel", "Piedra", "Papel"]
    assert partida_ppt(l1, l2) == 1