from herencia.multiple.saruman_soldier import SarumanSoldier


def test_saruman_soldier():
    mySS = SarumanSoldier(34, 3, "Orcland")
    assert mySS.attack() == "3 Attack!!!!!"
    assert mySS.shout() == "For Orcland!!!!!"
    assert True

