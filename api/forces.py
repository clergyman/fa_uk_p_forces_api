from api import config
import requests
__endpoint__ = "forces"


def get_all_forces():
    url = "/".join([config.__base_url__, __endpoint__])
    x = requests.get(url)
    return x.json()


def get_force_by_id(force_id):
    url = "/".join([config.__base_url__, __endpoint__, force_id])
    x = requests.get(url)
    return x.json()

