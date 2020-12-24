'''
Python3 Library for Fuzzwork api interaction
'''

import json
import requests

fuzzwork_URL = "https://www.fuzzwork.co.uk/"
blueprint_lookup_url = "blueprint/api/blueprint.php?typeid="
type_id_lookup_url = "api/typeid.php?typename="


def get_type_id_from_name(name: str) -> int:
    """
    Returns an id from a name
    :param name:
    :return:
    """
    id = requests.get(fuzzwork_URL+type_id_lookup_url+name).json()['typeID']
    return id


def get_blueprint_properties(item_id: int) -> json:
    """
    Get the blue print properties.
    :type item_id: ID for blueprint
    """
    blueprint_json = requests.get(fuzzwork_URL+blueprint_lookup_url+str(item_id)).json()
    return blueprint_json


def get_blueprint_build_components(bp_prop: dict) -> dict:
    """
    Gets the build components of a blueprint material build list
    :param bp_prop: blue print propertz
    :return:
    """
    return bp_prop['activityMaterials']['1']

def is_buildable(object: json) -> bool:
    """
    Checks if the object is a component/reaction that has an associated blueprint
    :type object: object
    :param object:
    :return:
    """
    if object['maketype'] > -1:
        return True
    return False



