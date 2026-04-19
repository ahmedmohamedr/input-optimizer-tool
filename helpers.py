import numpy as np
import random

def normalize_input(input_data):
    max_val = np.max(input_data)
    min_val = np.min(input_data)
    return (input_data - min_val) / (max_val - min_val) if max_val > min_val else input_data


def random_sample(input_data, sample_size):
    return random.sample(input_data, sample_size) if sample_size <= len(input_data) else input_data


def batch_process(inputs, batch_size):
    return [inputs[i:i + batch_size] for i in range(0, len(inputs), batch_size)]


def generate_statistics(input_data):
    mean = np.mean(input_data)
    median = np.median(input_data)
    variance = np.var(input_data)
    return {'mean': mean, 'median': median, 'variance': variance}


def shuffle_data(input_data):
    shuffled = input_data[:]
    random.shuffle(shuffled)
    return shuffled