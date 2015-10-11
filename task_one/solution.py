"""FMI Python task one solution. """
def interpret_western_sign(day, month):
    """Determine the western sign given an integer day and month."""
    signs = {
        'aquarius': range(121, 220),
        'pisces': range(220, 321),
        'aries': range(321, 421),
        'taurus': range(421, 521),
        'gemini': range(521, 621),
        'cancer': range(621, 723),
        'leo': range(723, 823),
        'virgo': range(823, 923),
        'libra': range(923, 1023),
        'scorpio': range(1023, 1122),
        'sagittarius': range(1122, 1222)
    }

    for sign, dates in signs.items():
        if month * 100 + day in dates:
            return sign
    return 'capricorn'


def interpret_chinese_sign(year):
    """Determin the chinese sign given a year"""
    signs = [
        'rat', 'ox', 'tiger',
        'rabbit', 'dragon',
        'snake', 'horse',
        'sheep', 'monkey',
        'rooster', 'dog', 'pig'
    ]

    return signs[(year - 1900) % 12]


def interpret_both_signs(day, month, year):
    """Determine both the western and chinese sign given a date and a year"""
    return (interpret_western_sign(day, month), interpret_chinese_sign(year))

print(interpret_chinese_sign(0))
