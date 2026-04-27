import random
import numpy as np


def clamp(value, min_value, max_value):
    return max(min(value, max_value), min_value)


def scale_vector(vec, scale):
    return [coord * scale for coord in vec]


def weighted_random_choice(choices):
    total = sum(weight for item, weight in choices)
    threshold = random.uniform(0, total)
    cumulative_weight = 0
    for item, weight in choices:
        cumulative_weight += weight
        if cumulative_weight >= threshold:
            return item


def normalize_vector(vec):
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec
    return [coord / norm for coord in vec]


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def lerp(start, end, t):
    return start + (end - start) * t