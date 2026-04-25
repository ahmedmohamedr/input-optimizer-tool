def optimize_input(user_input):
    try:
        if not isinstance(user_input, str):
            raise TypeError('Input must be a string.')
        if len(user_input) == 0:
            raise ValueError('Input cannot be an empty string.')
        optimized = user_input.strip().lower()
        if optimized == '':
            raise ValueError('Input cannot be just whitespace.')
        return optimized
    except TypeError as te:
        return f'Error: {te}'
    except ValueError as ve:
        return f'Error: {ve}'
    except Exception as e:
        return f'Unexpected error: {e}'

if __name__ == '__main__':
    print(optimize_input('  Hello World!  '))  # expected output: 'hello world!'
    print(optimize_input(''))  # expected output: 'Error: Input cannot be an empty string.'
    print(optimize_input(123))  # expected output: 'Error: Input must be a string.'
    print(optimize_input('    '))  # expected output: 'Error: Input cannot be just whitespace.'
    