from api import forces
import validators
from data import mock_forces


#all_forces = forces.get_all_forces()
#for f in all_forces:
    #print(f)
    #f_site = mock_forces.mock_force_by_id(f['id'])['url']
    #f['site'] = f_site
    
all_forces = forces.get_all_forces()
for f in all_forces:
    f_by_id = forces.get_force_by_id(f['id'])
    if 'url' in f_by_id:
        f_site = f_by_id['url']
    else:
        f_site = None
    f['site'] = f_site

def test_all_forces_have_site():
    errors = []
    for _ in all_forces:
        if _['site'] is None:
            errors.append("Police force {}: no website".format(_['id']))
    assert not errors, "errors occured:\n{}".format("\n".join(errors))


def test_all_site_urls_are_valid():
    errors = []
    for _ in all_forces:
        print(_)
        v = validators.url(_['site'])
        if not v:
            errors.append("Police force {}: website is not valid: {}".format(_['name'], _['site']))

    print(errors)
    assert not errors, "errors occured:\n{}".format("\n".join(errors))