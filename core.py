import time
import numpy as np

class PerformanceOptimizer:
    def __init__(self, data):
        self.data = np.array(data)

    def optimize(self):
        # Vectorized operation for speed
        start_time = time.time()
        optimized_data = self._process_data(self.data)
        elapsed_time = time.time() - start_time
        print(f'Optimization completed in {elapsed_time:.4f} seconds')
        return optimized_data

    def _process_data(self, data):
        return data[data > 0] * 10  # Example of optimization

if __name__ == '__main__':
    sample_data = list(range(-10, 10))  # Sample input data
    optimizer = PerformanceOptimizer(sample_data)
    optimized_result = optimizer.optimize()
    print(optimized_result)