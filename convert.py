from typing import Tuple

def cmyk_to_rgb(c: float, m: float, y: float, k: float) -> Tuple[int, int, int]:
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    return round(r), round(g), round(b)

def rgb_to_cmyk(r: int, g: int, b: int) -> Tuple[float, float, float, float]:
    r /= 255.0
    g /= 255.0
    b /= 255.0
    k = 1 - max(r, g, b)
    if k < 1:
        c = (1 - r - k) / (1 - k)
        m = (1 - g - k) / (1 - k)
        y = (1 - b - k) / (1 - k)
    else:
        c = m = y = 0
    return tuple(round(i, 2) for i in [c, m, y, k])