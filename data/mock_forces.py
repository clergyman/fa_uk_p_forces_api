import json

def all_mock_forces():
    with open('data/forces.json') as json_file: all_forces = json.load(json_file)
    return all_forces

def mock_force_by_id(force_id):
    with open("data/forces/{}.json".format(force_id)) as json_file: force = json.load(json_file)
    return force