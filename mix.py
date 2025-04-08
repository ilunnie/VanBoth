from typing import Tuple, Union

ink = Tuple[float, float, float, float]

def complete_percents(*colors: Union[ink, Tuple[ink, float]]):
    colors = list(colors)
    indexes = []
    mixes = 0
    for i in range(len(colors)):
        color = colors[i]
        if len(color) == 4:
            indexes.append(i)
        else:
            assert color[1] >= 0
            mixes += color[1]
    if len(indexes) > 0:
        assert mixes <= 1
        remainder = (1 - mixes) / len(indexes)
        for i in indexes:
            colors[i] = (colors[i], remainder)
        mixes = 1
    assert mixes == 1
    return tuple(colors)

def mix(*colors: Union[ink, Tuple[ink, float]]):
    colors = complete_percents(*colors)
    cmyk = [((c * p), (m * p), (y * p), (k * p))
            for (c, m, y, k), p
            in colors]
    return tuple(map(sum, zip(*cmyk)))