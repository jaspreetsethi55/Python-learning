import pytest


@pytest.mark.parametrize("device_type",['mna-540'])
@pytest.mark.parametrize("mirror_mode",['H','NONE'])
def test_m1(device_type,mirror_mode):
    assert 2==3, [device_type,mirror_mode]
