from api import forces

def test_all():
    forces.get_all_forces()
    forces.get_force_by_id("bedfordshire")
    forces.open_force_site("http://www.bes.police.uk")
    assert False
