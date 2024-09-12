def mapping(value, min_a, max_a, min_b, max_b, dtype=int):
    return dtype(value * (max_b - min_b) / (max_a - min_a) + (min_b - min_a))