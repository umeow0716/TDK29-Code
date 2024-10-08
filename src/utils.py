def mapping(value, min_a, max_a, min_b, max_b, dtype=int):
    return dtype((value - min_a) / (max_a - min_a) * (max_b - min_b) + min_b)