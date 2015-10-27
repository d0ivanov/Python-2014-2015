def fibonacci():
    previous, following = 1, 1
    while True:
        yield previous
        previous, following = following, previous + following


def primes():
    prime = 2
    while True:
        for i in range(2, prime):
            if prime % i == 0:
                break
        else:
            yield prime
        prime += 1


def alphabet(**kwargs):
    if 'letters' in kwargs.keys():
        for letter in kwargs['letters']:
            yield letter
    else:
        start, end = ord('a'), ord('z')
        if kwargs['code'] == 'bg':
            start, end = ord('а'), ord('я')
        while start <= end:
            if start == ord('э') or start == ord('ы'):
                start = ord(start) + 1
            yield chr(start)
            start += 1


def get_args(sequence):
    args = {}
    keys = list(set(list(sequence)) - set(['sequence', 'length']))
    for key in keys:
        args[key] = sequence[key]
    return args


def intertwined_sequences(sequences, generator_definitions={}):
    generators = {}
    for sequence in sequences:
        name = sequence['sequence']
        args = get_args(sequence)
        if name in globals().keys() and name not in generators.keys():
            generator = globals()[name]
            generators[name] = generator(**args)
        elif name not in generators.keys():
            generator = generator_definitions[name]
            generators[name] = iter(generator(**get_args(sequence)))
        i = 0
        while i < sequence['length']:
            yield next(generators[name])
            i += 1
