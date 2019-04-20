from skconfig.parameter import BoolParam


def test_bool_param_type():
    p = BoolParam()
    f = BoolParam()
    assert p.value_type == bool
    assert f.access_type == False
