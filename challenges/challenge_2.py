def pickles(count, pickle):
    i = 0
    while i < count:
        yield pickle
        i += 1


def take(count, pickle):
    i = 0
    while i < count:
        yield next(pickle)
        i += 1


def jar(bell_peppers, cauliflowers, carrots, celeries):
    for pepper in take(1, bell_peppers):
        yield pepper
    for cauliflower in take(2, cauliflowers):
        yield cauliflower
    for carrot in take(4, carrots):
        yield carrot
    for celerie in take(3, celeries):
        yield celerie


def jars_content(jars, bell_peppers, cauliflowers, carrots, celeries):
    peppers = pickles(bell_peppers, 'bell_pepper')
    cauliflowers = pickles(cauliflowers, 'cauliflower')
    carrots = pickles(carrots, 'carrot')
    celeries = pickles(celeries, 'celery')

    return [jar(peppers, cauliflowers, carrots, celeries) for _ in range(jars)]
