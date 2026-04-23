class InputProcessor:
    def __init__(self, config):
        self.config = config

    def process_inputs(self, raw_inputs):
        clean_inputs = self._cleanup(raw_inputs)
        optimized_inputs = self._optimize(clean_inputs)
        return optimized_inputs

    def _cleanup(self, inputs):
        return [input.strip() for input in inputs if input]

    def _optimize(self, inputs):
        return list(set(inputs))

if __name__ == '__main__':
    sample_inputs = ['  jump', 'run ', '   ', 'run ', 'crouch']
    processor = InputProcessor(config={})
    optimized = processor.process_inputs(sample_inputs)
    print(optimized)