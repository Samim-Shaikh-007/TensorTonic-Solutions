import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    a = np.array(a,dtype = float)
    b = np.array(b,dtype = float)

    Dot = float(sum(a*b))

    mag_a = float(sum(a*a))**0.5
    mag_b = float(sum(b*b))**0.5

    if mag_a == 0 or mag_b == 0:
        return 0.0
    cos_theta = Dot/(mag_a*mag_b)

    return float(cos_theta)