import pytest
import validators
import tldextract

from itertools import groupby

from conftest import data_source
from api import forces
from data import mock_forces
from util import site_available


@pytest.fixture
def all_forces(data_source):
    if data_source == 'mock':
        res = mock_forces.all_mock_forces()
        for f in res:
            f_by_id = mock_forces.mock_force_by_id(f['id'])
            if 'url' in f_by_id:
                f_site = f_by_id['url']
            else:
                f_site = None
            f['site'] = f_site
    else:
        res = forces.get_all_forces()
        for f in res:
            f_by_id = forces.get_force_by_id(f['id'])
            if 'url' in f_by_id:
                f_site = f_by_id['url']
            else:
                f_site = None
            f['site'] = f_site
    return res


########################################################################
# Test that all elements of forces list have 'url' key in the response #
########################################################################
def test_all_forces_have_site(all_forces):
    errors = []
    for _ in all_forces:
        if _['site'] is None:
            errors.append("Police force {}: no website".format(_['id']))
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

########################################################################
# Test that all department urls are really valid urls                  #
########################################################################
def test_all_site_urls_are_valid(all_forces):
    errors = []
    for _ in all_forces:
        if _['site']: v = validators.url(_['site'])
        if not v:
            errors.append("Police force {}: website is not valid: {}".format(_['name'], _['site']))

    assert not errors, (
        "errors occured:\n{}".format(len(errors), "\n".join(errors))
    )


########################################################################
# Test that all department urls are <something>.police.uk<something>   #
########################################################################
def test_all_sites_are_in_police_uk_domain(all_forces):
    errors = []
    for _ in all_forces:
        if _['site'] and validators.url(_['site']):
            url_extract = tldextract.extract(_['site'])
            if url_extract.suffix != 'police.uk':
                errors.append(
                    "Police force {}: website is not in \"police.uk\" domain: {}".format(_['name'], _['site']))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

########################################################################
# Test that all urls refer to existing site in the Internet            #
########################################################################
def test_all_sites_are_available(all_forces):
    errors = []
    for _ in all_forces:
        if not site_available(_['site']):
            errors.append("Police force {}: website is not available: {}".format(_['name'], _['site']))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))

########################################################################
# Test that all urls sre unique                                        #
########################################################################
def test_all_sites_are_unique(all_forces):
    sorted_forces = sorted(all_forces, key=lambda d: d['id'])
    errors = []

    for key, value in groupby(sorted_forces, lambda d: d['site']):
        if list(value).__len__() > 1:
            errors.append("Police force site is not unique {}".format(key))

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
