import pytest
import fuzzwork


@pytest.mark.parametrize(
    "name, expected_id",
    [("Sabre Blueprint", 22457),
     ("Fulleride Reaction", 17967)]
)
def test_get_type_id(name, expected_id):
    id = fuzzwork.get_type_id_from_name(name)
    assert id == expected_id


@pytest.mark.parametrize("name",
                         [("Sabre Blueprint"), ("Fulleride Reaction")]
                         )
def test_get_blueprint_properties(name):
    bp_properties = fuzzwork.get_blueprint_properties(fuzzwork.get_type_id_from_name(name))
    assert isinstance(bp_properties, dict)


@pytest.mark.parametrize("build_comp_list", [(fuzzwork.get_blueprint_properties(
    fuzzwork.get_type_id_from_name("Sabre Blueprint"))['activityMaterials']['1'])])
def test_is_component(build_comp_list):
    errorlist = []

    for buildcomp in build_comp_list:
        if fuzzwork.is_buildable(buildcomp) == True:
            continue
        errorlist.append(buildcomp['name'])

    assert errorlist == ['Morphite', 'Construction Blocks']
