import os

import infomap.main as info


def test_read_json():
    dat = info.read_json(os.path.join('./tests/data/sample_data.json'))
    assert dat == {'CAN': '20', 'USA': '10'}
